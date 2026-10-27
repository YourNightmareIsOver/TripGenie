# Cloud Deployment 40476984860: current evidence

Captured 2026-10-27T09:06:00.912677+00:00. [Workflow run](https://github.com/YourNightmareIsOver/TripGenie/actions/runs/40476984860).

| Field | Result |
| --- | --- |
| Deployed commit | `7bcedc9860cabbf4f1ab378c368102c36a1c9be2` (merge of PR #189) |
| Trigger / branch | `workflow_dispatch` / `main` |
| Created / completed (UTC) | 2026-10-27T08:55:54Z / 2026-10-27T09:03:02Z |
| Workflow | Success; all 17 jobs succeeded |
| Cloud checks | 41 validation rows and six security-configuration rows passed |
| Student 1 endpoint suite | 7 passed; 0 failures, errors or skips; 0.220 seconds |
| Live Azure state | 18 apps at the intended image; each latest revision equals its latest ready revision |
| Public / internal | Six public HTTPS frontends; twelve internal services |

## Deploy-job steps

| Step | Started (UTC) | Completed (UTC) | Result |
| --- | --- | --- | --- |
| Set up job | 2026-10-27T08:57:56Z | 2026-10-27T08:57:57Z | success |
| Run actions/checkout@v4 | 2026-10-27T08:57:57Z | 2026-10-27T08:57:58Z | success |
| Azure login | 2026-10-27T08:57:58Z | 2026-10-27T08:58:03Z | success |
| Set up deployment environment | 2026-10-27T08:58:03Z | 2026-10-27T08:58:05Z | success |
| Build and push images | 2026-10-27T08:58:05Z | 2026-10-27T09:01:06Z | success |
| Azure login (refresh) | 2026-10-27T09:01:06Z | 2026-10-27T09:01:07Z | success |
| Create Container Apps environment | 2026-10-27T09:01:07Z | 2026-10-27T09:01:11Z | success |
| Azure login (refresh again) | 2026-10-27T09:01:11Z | 2026-10-27T09:01:12Z | success |
| Deploy to Azure Container Apps | 2026-10-27T09:01:12Z | 2026-10-27T09:02:32Z | success |
| Validate deployment and generate evidence | 2026-10-27T09:02:32Z | 2026-10-27T09:02:57Z | success |
| Publish deployment results | 2026-10-27T09:02:57Z | 2026-10-27T09:02:57Z | success |
| Upload deployment evidence | 2026-10-27T09:02:57Z | 2026-10-27T09:02:58Z | success |
| Post Azure login (refresh again) | 2026-10-27T09:02:58Z | 2026-10-27T09:02:59Z | success |
| Post Azure login (refresh) | 2026-10-27T09:02:59Z | 2026-10-27T09:02:59Z | success |
| Post Azure login | 2026-10-27T09:02:59Z | 2026-10-27T09:02:59Z | success |
| Post Run actions/checkout@v4 | 2026-10-27T09:02:59Z | 2026-10-27T09:02:59Z | success |
| Complete job | 2026-10-27T09:02:59Z | 2026-10-27T09:02:59Z | success |

## Intended-image revision gate

The following lines were extracted from the real deployment job log.
All images end in the full deployed SHA above; the separate Azure read
confirmed that each remains the app's latest ready revision.

| App | Ready revision |
| --- | --- |
| shared-backend | `shared-backend--0000014` |
| shared-database | `shared-database--0000011` |
| shared-ui | `shared-ui--0000012` |
| student-1-backend | `student-1-backend--0000014` |
| student-1-database | `student-1-database--0000012` |
| student-1-frontend | `student-1-frontend--0000013` |
| student-2-backend | `student-2-backend--0000014` |
| student-2-database | `student-2-database--0000014` |
| student-2-frontend | `student-2-frontend--0000012` |
| student-3-backend | `student-3-backend--0000014` |
| student-3-database | `student-3-database--0000014` |
| student-3-frontend | `student-3-frontend--0000013` |
| student-4-backend | `student-4-backend--0000013` |
| student-4-database | `student-4-database--0000012` |
| student-4-frontend | `student-4-frontend--0000011` |
| student-5-backend | `student-5-backend--0000014` |
| student-5-database | `student-5-database--0000012` |
| student-5-frontend | `student-5-frontend--0000012` |

## Live frontend screenshots

Real Chrome viewport captures after Azure state verification; no DOM edits.
All six returned HTTP 200 without an HTTP (non-TLS) subrequest.
These are read-only page loads, not a fresh Students 2-5 CRUD cycle.

| App | HTTP | Page title | Screenshot |
| --- | --- | --- | --- |
| [shared-ui](https://shared-ui.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io) | 200 | TripGenie | [PNG](screenshots/shared-ui.png) |
| [student-1-frontend](https://student-1-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io) | 200 | Hobart Weekend Escape · TripGenie Student 1 | [PNG](screenshots/student-1-frontend.png) |
| [student-2-frontend](https://student-2-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io) | 200 | Accommodation · TripGenie Student 2 | [PNG](screenshots/student-2-frontend.png) |
| [student-3-frontend](https://student-3-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io) | 200 | Browse transport · TripGenie Student 3 | [PNG](screenshots/student-3-frontend.png) |
| [student-4-frontend](https://student-4-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io) | 200 | Activities & Attractions · TripGenie Student 4 | [PNG](screenshots/student-4-frontend.png) |
| [student-5-frontend](https://student-5-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io) | 200 | Budgets · TripGenie Student 5 | [PNG](screenshots/student-5-frontend.png) |

## Original sources and screenshots

- [Unchanged full deployment artifact](cloud-deployment-results.md)
- [Unchanged Student 1 endpoint report](student-1-endpoint-tests.md)
- [Unchanged Student 1 JUnit XML](student-1-endpoint-tests.xml)
- [GitHub run screenshot](screenshots/cloud-run.png)
- [Complete deployment artifact screenshot](screenshots/cloud-deployment-results.png)
- [Complete endpoint artifact screenshot](screenshots/student-1-endpoint-tests.png)
- [Run/job/step metadata](run-metadata.json)
- [Artifact names and retention](artifact-index.json)
- [Read-only Azure state](azure-state.json)
- [Current production protections](production-environment.json)
- [Production branch policy](production-branch-policy.json)
- [Current observed cost](cost-summary.md)

The artifact retains its original pending-review sentence. Do not equate
the automated deployment result with a new model review or human sign-off.
No tenant, subscription, client or principal identifiers are published.
