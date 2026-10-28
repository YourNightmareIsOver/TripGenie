# Student 3 Post-Commit CI/CD Testing Report

Release 2, post-commit testing. Student 3 owns the Transport service. Its
workflow, `.github/workflows/student-3-ci.yml`, runs automated endpoint tests
for two backend functions after every push or pull request that touches
`student-3/**`, `shared/configuration/**`, the workflow itself or
`docker-compose.yml` (PR #192).

| | |
| --- | --- |
| Run | [Student 3 CI, run 40476908116](https://github.com/YourNightmareIsOver/TripGenie/actions/runs/40476908116/job/122097274311) |
| Event | `push` to `main` (merge of PR #189) |
| Commit | `7bcedc9860cabbf4f1ab378c368102c36a1c9be2` |
| Job | `Validate Student 3 Compose Integration`: success |
| Command | `python -m pytest tests/endpoint --junitxml=student-3-endpoint-tests.xml -v` |
| Target | `http://127.0.0.1:18003` (the Compose backend) |
| Artifact | `student-3-endpoint-test-evidence` (JUnit XML and Markdown summary) |
| Result | **11 passed, 0 failed, 0 errors, 0 skipped** in 0.42s |

## Endpoints under test and why

| Endpoint | Function | Why it was chosen |
| --- | --- | --- |
| `POST /api/transport-options` then `GET /api/transport-options/{id}` | Create and read a transport option | This is the core catalogue write. The backend validates the route and times, derives `duration_minutes` and the pricing basis, and stores the option in the database service. Transport ids are what Student 1 itineraries refer to (`transport_client.py`). |
| `GET /api/transport-options/compare` | Compare transport options | This is the service's main decision-support read. The Student 3 frontend's compare page and the shared MCP `transport_compare` tool both call it with up to four option ids. |

## Test cases

File: `student-3/tests/endpoint/test_post_commit_endpoints.py`. The tests call
the live backend over HTTP; nothing is mocked. Each test that needs an option
creates one with a unique `transport_ci_<random>` id and deletes it afterwards,
so reruns against the same stack start clean. The compare tests also use two
options seeded by the database service.

| # | Endpoint | Test | Checks |
| --- | --- | --- | --- |
| 1 | `POST`/`GET /transport-options` | `test_a_created_option_is_stored_and_read_back` | `POST` returns 201. `GET /transport-options/{id}` returns 200 and exactly the created option: price `48.75`, a derived `duration_minutes` of 210 and pricing basis `per_traveller`. |
| 2 | `POST /transport-options` | `test_a_created_option_appears_in_the_filtered_list` | The created option appears in `GET /transport-options` filtered by its provider and origin (200). |
| 3 | `POST /transport-options` | `test_an_option_going_nowhere_is_rejected` | A destination equal to the origin (ignoring case and spaces) is rejected with 422 `VALIDATION_ERROR` on `destination`. |
| 4 | `POST /transport-options` | `test_an_option_arriving_before_it_departs_is_rejected` | An arrival before the departure is rejected with 422. |
| 5 | `GET /transport-options/{id}` | `test_an_unknown_option_is_not_found` | An unused id returns 404 `NOT_FOUND`. |
| 6 | `GET /transport-options/compare` | `test_compare_returns_the_options_in_departure_order` | Two seeded options sent in reverse come back in departure order (200). |
| 7 | `GET /transport-options/compare` | `test_compare_includes_a_newly_created_option` | A seeded option and the newly created one are both returned (200). |
| 8 | `GET /transport-options/compare` | `test_compare_reports_an_unknown_option` | An unknown id in the selection returns 404 `NOT_FOUND`. |
| 9-11 | `GET /transport-options/compare` | `test_compare_rejects_an_invalid_selection` | More than four ids, a repeated id and a malformed id are each rejected with 422 on `ids`. |

Errors use the service's standard envelope:
`{"error": {"code", "message", "details": [{"field", "issue"}]}}`.

## How it runs in `student-3-ci.yml`

The `compose` job runs with the MCP, RAG and multi-agent integrations turned
off, because no host AI services exist on the runner. It:

1. builds and starts `student-3-database`, `student-3-backend` and
   `student-3-frontend` with `docker compose up -d --build --no-deps`, and
   waits for the frontend's `/ready`;
2. checks that the shared home page links the published frontend port, and
   that MCP, RAG and multi-agent report that they are disabled;
3. **Post-commit endpoint tests**: from `student-3/`, runs the command above
   against the backend on host port 18003. A failing test fails the job;
4. **Endpoint test summary** (`if: always()`): turns the JUnit XML into a
   pass/fail table in the job summary and in `student-3-endpoint-tests.md`;
5. **Upload endpoint test evidence** (`if: always()`): uploads the XML and the
   Markdown file as `student-3-endpoint-test-evidence`, even when tests fail;
6. prints the Compose logs if any step failed, then tears the stack down with
   `docker compose down -v`.

The test fixture first calls the backend's `/ready` and raises on any
connection or HTTP error, so an unavailable backend produces test errors and a
failed job, never a silent pass. `tests/endpoint` is not in the `testpaths` in
`student-3/pyproject.toml`, so ordinary runs of `pytest` in `student-3/` do not
need a live backend.

## CI result

From the uploaded `student-3-endpoint-tests.md`:

| Test | Result |
| --- | --- |
| `test_a_created_option_is_stored_and_read_back` | PASS |
| `test_a_created_option_appears_in_the_filtered_list` | PASS |
| `test_an_option_going_nowhere_is_rejected` | PASS |
| `test_an_option_arriving_before_it_departs_is_rejected` | PASS |
| `test_an_unknown_option_is_not_found` | PASS |
| `test_compare_returns_the_options_in_departure_order` | PASS |
| `test_compare_includes_a_newly_created_option` | PASS |
| `test_compare_reports_an_unknown_option` | PASS |
| `test_compare_rejects_an_invalid_selection[more-than-four]` | PASS |
| `test_compare_rejects_an_invalid_selection[repeated]` | PASS |
| `test_compare_rejects_an_invalid_selection[malformed]` | PASS |

## Running locally

From the repository root, with Docker running:

```bash
docker compose up -d --build --wait --no-deps student-3-database student-3-backend student-3-frontend
python -m pip install -e "./student-3[dev]"
cd student-3
STUDENT3_ENDPOINT_BASE_URL=http://127.0.0.1:18003 python -m pytest tests/endpoint -v
```
