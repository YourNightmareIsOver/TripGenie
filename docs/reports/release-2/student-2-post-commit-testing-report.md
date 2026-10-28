# Student 2 Post-Commit CI/CD Testing Report

Release 2, post-commit testing. Student 2 owns the Accommodation service. Its
workflow, `.github/workflows/student-2-ci.yml`, runs automated endpoint tests
for two backend functions after every push or pull request that touches
`student-2/**`, `shared/**`, the AI-Mode or RAG server sources, the workflow
itself or `docker-compose.yml` (PR #207).

| | |
| --- | --- |
| Run | [Student 2 CI, run 40483973852](https://github.com/YourNightmareIsOver/TripGenie/actions/runs/40483973852/job/122121005611) |
| Event | `push` to `main` (merge of PR #207) |
| Commit | `b84d2008cf68f57609f90e3ac9eb06bf6bc9f2fe` |
| Job | `Student 2 Post-Commit Endpoint Tests`: success |
| Command | `python -m pytest tests/endpoint --junitxml=student-2-endpoint-tests.xml -v` |
| Target | `http://127.0.0.1:9000` (the Compose backend) |
| Artifact | `student-2-endpoint-test-evidence` (JUnit XML and Markdown summary) |
| Result | **7 passed, 0 failed, 0 errors, 0 skipped** in 0.22s |

## Endpoints under test and why

| Endpoint | Function | Why it was chosen |
| --- | --- | --- |
| `POST /accommodation` | Create an accommodation | This is the core catalogue write. An accommodation crosses every layer: the backend validates it, resolves its country and city through the shared reference service, and stores it in the database service. Accommodation ids are what Student 1 itineraries refer to. |
| `GET /accommodation/{id}` | Read an accommodation | This is the main read path for a single stay. The Student 2 frontend's detail modal and Student 1's backend (`accommodation_client.py`) both resolve an accommodation by id through it. |

## Test cases

File: `student-2/tests/endpoint/test_post_commit_endpoints.py`. The tests call
the live backend over HTTP; nothing is mocked. Each test that needs an
accommodation creates one with a unique `CI Endpoint Stay <random>` name and
deletes it afterwards, so reruns against the same stack start clean.

| # | Endpoint | Test | Checks |
| --- | --- | --- | --- |
| 1 | `POST`/`GET /accommodation` | `test_create_accommodation_returns_201_and_reads_back` | `POST` returns 201 with the sent name. `GET /accommodation/{id}` returns 200 with the same name and the city resolved as `sydney`. |
| 2 | `POST /accommodation` | `test_created_accommodation_is_listed` | The created accommodation's id appears in `GET /accommodation` (200), and `total` is at least 1. |
| 3 | `POST /accommodation` | `test_create_accommodation_rejects_missing_name` | A payload without a name is rejected with 400 or 422. |
| 4 | `POST /accommodation` | `test_create_accommodation_rejects_unknown_city` | A city the shared reference service does not know is rejected with 400. |
| 5 | `GET /accommodation/{id}` | `test_get_accommodation_returns_full_message` | Returns 200 with the same id, the sent nightly price and availability status `available`. |
| 6 | `GET /accommodation/{id}` | `test_get_unknown_accommodation_returns_404` | A random, unused id returns 404. |
| 7 | `GET /accommodation/{id}` | `test_deleted_accommodation_is_gone` | After `DELETE /accommodation/{id}` returns 204, `GET` for the same id returns 404. |

The expected status codes follow `student-2/docs/backend-service-api.md`.

## How it runs in `student-2-ci.yml`

The `compose` job runs with the MCP, RAG and multi-agent integrations turned
off, because no host AI services exist on the runner. It:

1. builds and starts `shared-database`, `shared-backend`, `student-2-database`
   and `student-2-backend` with `docker compose up -d --build --no-deps`.
   The shared reference service is included because accommodations store
   shared location ids and the backend resolves names through it;
2. waits for the backend's `/health` on host port 9000;
3. **Post-commit endpoint tests**: from `student-2/`, runs the command above
   against the backend. A failing test fails the job;
4. **Endpoint test summary** (`if: always()`): turns the JUnit XML into a
   pass/fail table in the job summary and in `student-2-endpoint-tests.md`;
5. **Upload endpoint test evidence** (`if: always()`): uploads the XML and the
   Markdown file as `student-2-endpoint-test-evidence`, even when tests fail;
6. prints the shared and Student 2 service logs if any step failed.

The test fixture first calls the backend's `/health` and raises on any
connection or HTTP error, so an unavailable backend produces test errors and a
failed job, never a silent pass. `tests/endpoint` is not in the `testpaths` in
`student-2/pyproject.toml`, so ordinary runs of `pytest` in `student-2/` do not
need a live backend.

## CI result

From the uploaded `student-2-endpoint-tests.md`:

| Test | Result |
| --- | --- |
| `test_create_accommodation_returns_201_and_reads_back` | PASS |
| `test_created_accommodation_is_listed` | PASS |
| `test_create_accommodation_rejects_missing_name` | PASS |
| `test_create_accommodation_rejects_unknown_city` | PASS |
| `test_get_accommodation_returns_full_message` | PASS |
| `test_get_unknown_accommodation_returns_404` | PASS |
| `test_deleted_accommodation_is_gone` | PASS |

## Running locally

From the repository root, with Docker running:

```bash
docker compose up -d --build --wait --no-deps shared-database shared-backend student-2-database student-2-backend
python -m pip install -e "./student-2[dev]"
cd student-2
STUDENT2_ENDPOINT_BASE_URL=http://127.0.0.1:9000 python -m pytest tests/endpoint -v
```
