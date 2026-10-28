# Student 4 Post-Commit CI/CD Testing Report

Release 2, post-commit testing. Student 4 owns the Activities and Attractions
service. Its workflow, `.github/workflows/student-4-ci.yml`, runs automated
endpoint tests for two backend functions after every push or pull request that
touches `student-4/**`, the workflow itself or `docker-compose.yml` (PR #205).

| | |
| --- | --- |
| Run | [Student 4 CI, run 40645907239](https://github.com/YourNightmareIsOver/TripGenie/actions/runs/40645907239/job/122674542044) |
| Event | `push` to `main` (merge of PR #205) |
| Commit | `220001452e2018f73157c1733c06b102ca1057a5` |
| Job | `Validate Student 4 Compose Integration`: success |
| Command | `python -m pytest tests/endpoint --junitxml=student-4-endpoint-tests.xml -v` |
| Target | `http://127.0.0.1:18008` (the Compose backend) |
| Artifact | `student-4-endpoint-test-evidence` (JUnit XML and Markdown summary) |
| Result | **6 passed, 0 failed, 0 errors, 0 skipped** in 0.26s |

## Endpoints under test and why

| Endpoint | Function | Why it was chosen |
| --- | --- | --- |
| `POST /activity` then `GET /activity/{id}` | Create and read an activity | This is the core catalogue write. An activity crosses every layer: the backend validates it, resolves its country and city through the shared reference service, and stores it in the database service as an exact decimal price. Activity ids are what Student 1 itineraries and Student 5 budgets refer to. |
| `QUERY /activity` | Search activities | This is the main read path. The Student 4 frontend's filter form and the shared MCP activity tools both search through it, combining text, location, category, price and party-size filters. |

## Test cases

File: `student-4/tests/endpoint/test_post_commit_endpoints.py`. The tests call
the live backend over HTTP; nothing is mocked. Each test that needs an activity
creates one with a unique `CI kayak <random>` name and deletes it afterwards, so
reruns against the same stack start clean.

| # | Endpoint | Test | Checks |
| --- | --- | --- | --- |
| 1 | `POST`/`GET /activity` | `test_a_created_activity_is_stored_and_read_back` | `POST` returns 201. `GET /activity/{id}` returns 200 and exactly the created activity: price `"89.50"`, pricing basis `PER_PERSON`, category `ADVENTURE`, and country and city names resolved back through the shared reference service. |
| 2 | `POST /activity` | `test_an_activity_with_an_unknown_category_is_rejected` | An unsupported category code is rejected with 400. |
| 3 | `GET /activity/{id}` | `test_an_unknown_activity_is_not_found` | A random, unused id returns 404. |
| 4 | `QUERY /activity` | `test_a_text_search_finds_the_created_activity` | A search combining the activity's name, a lowercase location, its category, a maximum price of `"100.00"` and a party size of 4 returns exactly that activity, with `total` 1. |
| 5 | `QUERY /activity` | `test_a_search_outside_the_filters_excludes_the_activity` | The same name with a party size of 20, above the activity's maximum of 8, returns no results. |
| 6 | `QUERY /activity` | `test_a_search_with_an_unsupported_category_is_rejected` | An unsupported category code in the filter is rejected with 400. |

The expected status codes follow `student-4/docs/backend-service-api.md`.

## How it runs in `student-4-ci.yml`

The `compose` job runs with the MCP, RAG and Smart Planner integrations turned
off, because no host AI services exist on the runner. It:

1. builds and starts `student-4-database`, `student-4-backend` and
   `student-4-frontend` with `docker compose up -d --build --no-deps`, and
   waits for the frontend's `/ready`;
2. checks that MCP, RAG and Smart Planner report that they are disabled;
3. starts `shared-database` and `shared-backend`, because activities store
   shared location ids and the backend resolves names through that service;
4. **Post-commit endpoint tests**: from `student-4/`, runs the command above
   against the backend on host port 18008. A failing test fails the job;
5. **Endpoint test summary** (`if: always()`): turns the JUnit XML into a
   pass/fail table in the job summary and in `student-4-endpoint-tests.md`;
6. **Upload endpoint test evidence** (`if: always()`): uploads the XML and the
   Markdown file as `student-4-endpoint-test-evidence`, even when tests fail;
7. prints the Student 4 and shared service logs if any step failed, then tears
   the stack down with `docker compose down -v`.

The test fixture first calls the backend's `/ready` and raises on any
connection or HTTP error, so an unavailable backend produces test errors and a
failed job, never a silent pass. The tests skip only when
`STUDENT4_ENDPOINT_BASE_URL` is unset. CI always sets it, while ordinary
offline runs of `pytest student-4/tests` stay unaffected.

## CI result

From the uploaded `student-4-endpoint-tests.md`:

| Test | Result |
| --- | --- |
| `test_a_created_activity_is_stored_and_read_back` | PASS |
| `test_an_activity_with_an_unknown_category_is_rejected` | PASS |
| `test_an_unknown_activity_is_not_found` | PASS |
| `test_a_text_search_finds_the_created_activity` | PASS |
| `test_a_search_outside_the_filters_excludes_the_activity` | PASS |
| `test_a_search_with_an_unsupported_category_is_rejected` | PASS |

The same tests also passed before the merge, in the PR's `pull_request` run
([run 40471398100](https://github.com/YourNightmareIsOver/TripGenie/actions/runs/40471398100)).

## Running locally

From the repository root, with Docker running:

```bash
docker compose up -d --build --wait --no-deps student-4-database student-4-backend shared-database shared-backend
python -m pip install -e "./student-4[dev]"
cd student-4
STUDENT4_ENDPOINT_BASE_URL=http://127.0.0.1:18008 python -m pytest tests/endpoint -v
```
