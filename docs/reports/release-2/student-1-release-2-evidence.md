# Student 1 Release 2: CI/CD and cloud deployment evidence

Evidence collected on **27 October 2026** from completed GitHub Actions runs.
The feature-branch CI evidence is from **23 October**. The cloud section now
covers the successful **27 October deployment after PR #189**, using the
verified evidence published in merged PR #186. This documentation update
does not trigger another deployment.

This pack supplies report-ready explanations, screenshots, the complete
original report text and JUnit results, exact run/commit references, and a
[Student 1 commit log](student-1-release-2-commit-log.md).

## Evidence and version index

| Evidence | Run / job | Application commit | Observed result |
| --- | --- | --- | --- |
| Student 1 feature-branch CI | [Run 39887108168](https://github.com/YourNightmareIsOver/TripGenie/actions/runs/39887108168), [Compose/endpoint job](https://github.com/YourNightmareIsOver/TripGenie/actions/runs/39887108168/job/120197749318) | `29239a10763950c8beeea6a80d0c4b327c0ce784`, PR #189 | Workflow success; 7 endpoint tests passed |
| Student 1 CI for the deployed version | [Run 40476984860](https://github.com/YourNightmareIsOver/TripGenie/actions/runs/40476984860) | `7bcedc9860cabbf4f1ab378c368102c36a1c9be2`, `main` | 7 endpoint tests passed before deployment |
| Azure deployment | [Run 40476984860](https://github.com/YourNightmareIsOver/TripGenie/actions/runs/40476984860) | `7bcedc9860cabbf4f1ab378c368102c36a1c9be2`, `main` | Workflow success; 41 validation checks and 6 security-configuration checks passed |

**These are not all the same application version.** The feature-branch CI
tested PR #189 before its merge. The newer cloud deployment includes the
merged planner code, but the cloud profile keeps the feature disabled and
does not deploy its host-only AI services. The endpoint artifact from the
new cloud run supplies matching-SHA test evidence for the deployed application.

## Post-commit CI/CD testing

### Text for the group report

Student 1's post-commit CI/CD tests exercise two backend functions:
`POST /api/trips` and `POST /api/trips/{trip_id}/itinerary-items`. The
`student-1-ci.yml` workflow starts the real frontend, backend and SQLite
database services through Docker Compose and runs HTTP endpoint tests.
The cases check successful creation and persisted reads, invalid trip dates,
missing required fields, unknown trips and itinerary dates outside the trip.
An unreachable backend or failed assertion fails the endpoint-test step.
JUnit XML and a Markdown result table are uploaded as
`student-1-endpoint-test-evidence`, including when the tests fail.

Run **39887108168**, triggered by a pull-request update to PR #189, completed
successfully on 23 October 2026 at commit `29239a1`. All **seven endpoint
tests passed, with zero failures, errors or skips**. The JUnit suite took
**0.204 seconds**; this is test execution time, not the complete CI workflow
duration. Separately, the deployment workflow reran Student 1's tests at
the deployed commit `7bcedc9` on 27 October, with **seven passes and no failures,
errors or skips** in **0.220 seconds**.

### Screenshot 1: actual GitHub Actions run page

![Student 1 CI shows Success and successful database, backend, frontend, RAG and Compose jobs](student-1-report-evidence/screenshots/ci-run.png)

*Figure 1. Unmodified browser viewport capture of the public
[Student 1 CI run](https://github.com/YourNightmareIsOver/TripGenie/actions/runs/39887108168).
The GitHub run number shown in the heading is #445; the API run ID is
39887108168. The page also contains runner/action deprecation warnings;
workflow success does not mean there were no warnings. Public viewers may
need to sign in to open individual job logs.*

### Screenshot 2: complete endpoint-test report

![All seven Student 1 endpoint tests pass, with source run, commit and capture details](student-1-report-evidence/screenshots/ci-endpoint-report.png)

*Figure 2. Browser-rendered copy of the complete original Markdown artifact,
with an added provenance header. This is not a fabricated GitHub UI screenshot.
The source report and machine-readable JUnit result are preserved below.*

| Function | Cases covered | Result |
| --- | --- | --- |
| Create trip | Valid fields persist and can be read; created trip is listed; reversed date range rejected; missing name rejected | 4 passed |
| Create itinerary item | Valid item appears on its trip day; unknown trip rejected; date outside the trip rejected | 3 passed |

Original files:

- [Complete feature-branch test report](student-1-report-evidence/ci/student-1-endpoint-tests.md)
- [Feature-branch JUnit XML](student-1-report-evidence/ci/student-1-endpoint-tests.xml)
- [Feature-branch run/job/step metadata](student-1-report-evidence/ci/run-metadata.json)
- [27 October deployed-version test report](https://github.com/YourNightmareIsOver/TripGenie/blob/2ff5baa43178189cf8bf5aada0b228bb993ff66a/docs/reports/release-2/cloud-evidence/2026-10-27/student-1-endpoint-tests.md)
- [27 October deployed-version JUnit XML](https://github.com/YourNightmareIsOver/TripGenie/blob/2ff5baa43178189cf8bf5aada0b228bb993ff66a/docs/reports/release-2/cloud-evidence/2026-10-27/student-1-endpoint-tests.xml)

The existing [post-commit testing report](student-1-post-commit-testing-report.md)
explains the implementation and earlier deliberate-failure demonstration.
This pack adds newer, version-labelled evidence; it does not rewrite those
historical results.

## Successful cloud deployment

### Text for the group report

The shared Cloud Deployment workflow **40476984860** successfully deployed
commit `7bcedc9`, the merge of PR #189, to **Azure Container Apps** in
`rg-tripgenie` on **27 October 2026**. It completed at **09:03:02 UTC /
20:03:02 AEDT**. A subsequent Azure read confirmed all **18 applications**
used the intended full-SHA image and each latest revision was also its latest
ready revision. Its generated report records **41 passing validation checks**
and **six passing security-configuration checks**. All six public frontends
returned HTTP 200. Student 1's trip create, read and delete flow succeeded,
deletion was confirmed, and its disabled RAG route returned HTTP 503.

The deployment also checked frontend security headers, HTTP-to-HTTPS
redirects, and public-domain responses for all twelve internal backend and
database services. Configuration validation confirmed that only the six
frontends were public, image pulls used a managed identity, the targeted
plain-setting credential check passed, and registry admin and anonymous
access were disabled. The report states that AI-Mode, MCP, RAG and the
Multi-Agent Server were not deployed. Student 1's AI features remain disabled;
the direct Student 3/5 AI paths still target an unavailable host-only service
rather than being explicitly switched off. These results establish the outcome
of this specific deployment, not continuous monitoring or cloud AI execution.

The [updated shared cloud report](https://github.com/YourNightmareIsOver/TripGenie/blob/2ff5baa43178189cf8bf5aada0b228bb993ff66a/docs/reports/release-2/cloud-deployment-report.md)
also includes corrected architecture/CI diagrams, fresh captures of all six
frontends and observed resource-group cost of **AUD 35.72**, including a
partial 27 October billing row. Its documentation merge, `2ff5baa`, is not
the application image SHA; the deployed application remains `7bcedc9`.

### Screenshot 3: actual successful deployment run

![GitHub Cloud Deployment run 40476984860 shows Success at deployed commit 7bcedc9](https://raw.githubusercontent.com/YourNightmareIsOver/TripGenie/2ff5baa43178189cf8bf5aada0b228bb993ff66a/docs/reports/release-2/cloud-evidence/2026-10-27/screenshots/cloud-run.png)

*Figure 3. Unmodified browser viewport capture of
[Cloud Deployment run 40476984860](https://github.com/YourNightmareIsOver/TripGenie/actions/runs/40476984860),
shown as run #7 in the GitHub heading. The source commit is `7bcedc9`, the
run duration is 7 minutes 8 seconds, and all 17 jobs succeeded.
This is the actual run page, not a locally reconstructed success screen.*

### Screenshot 4: complete generated deployment report

![Complete 27 October Azure report with all 41 validation rows, six security rows and original reviewer note](https://raw.githubusercontent.com/YourNightmareIsOver/TripGenie/2ff5baa43178189cf8bf5aada0b228bb993ff66a/docs/reports/release-2/cloud-evidence/2026-10-27/screenshots/cloud-deployment-results.png)

*Figure 4. Browser-rendered copy of the complete downloaded
`cloud-deployment-results.md`, with an added provenance header. The image
includes every validation/security row, frontend URL, deployment timestamp,
AI-off statement and original reviewer note. Open the image at full resolution
to read it, or use the accompanying Markdown rather than shrinking the entire
long image onto one PDF page.*

Current original files, pinned to the merged PR #186 evidence:

- [Complete generated cloud report, including all accompanying text](https://github.com/YourNightmareIsOver/TripGenie/blob/2ff5baa43178189cf8bf5aada0b228bb993ff66a/docs/reports/release-2/cloud-evidence/2026-10-27/cloud-deployment-results.md)
- [Deployment workflow/job/step metadata](https://github.com/YourNightmareIsOver/TripGenie/blob/2ff5baa43178189cf8bf5aada0b228bb993ff66a/docs/reports/release-2/cloud-evidence/2026-10-27/run-metadata.json)
- [Revision gate, six frontend captures and evidence index](https://github.com/YourNightmareIsOver/TripGenie/blob/2ff5baa43178189cf8bf5aada0b228bb993ff66a/docs/reports/release-2/cloud-evidence/2026-10-27/run-summary.md)

The original [23 October cloud report](student-1-report-evidence/cloud/cloud-deployment-results.md),
[run metadata](student-1-report-evidence/cloud/run-metadata.json),
[endpoint report](student-1-report-evidence/cloud-student-1-ci/student-1-endpoint-tests.md)
and [JUnit XML](student-1-report-evidence/cloud-student-1-ci/student-1-endpoint-tests.xml)
remain unchanged as **historical `4ed8621` evidence**, not the latest deployment.
The original cloud screenshots in `student-1-report-evidence/screenshots/`
are likewise retained as historical captures; Figures 3 and 4 now use the
new deployment's images above.

### Interpretation and boundaries

- The new artifact's timestamp is `2026-10-27T09:02:57Z` (20:02:57 AEDT).
  Its screenshots were captured after the successful 27 October deployment.
- The original `Reviewer Notes: (pending agentic-loop Cloud Deployment Review)`
  line is preserved, rather than editing the downloaded artifact. The
  [26 October Cloud Review](https://github.com/YourNightmareIsOver/TripGenie/blob/2085a97cc5a548765ba8a363d960cdb0bdff092f/docs/reports/release-2/agentic-loop/cloud-review.md)
  records Accept / READY for the **older run 39911331439 at `4ed8621`**.
  It is not a review of `7bcedc9`. The newer rollout was explicitly authorized,
  but no new interactive agentic-loop acceptance is claimed.
- A public-domain 404 is not sufficient proof of isolation on its own; use it
  alongside the internal-ingress configuration result.
- The portal still returns the unversioned `nginx` header. The artifact's
  passing banner check does not mean every server header is absent.
- The plain-setting credential scan checks credential-like environment names.
  It is not proof that every possible secret has been exhaustively audited.
- The `production` environment reference does not itself enforce a reviewer.
  A read-only check on 27 October found the `main` branch policy but no
  required-reviewer rule. These successful run screenshots must not be used
  as proof that required-reviewer protection is currently enabled.
- Frontend CRUD results do not prove durable database storage across a restart
  or deployment; the deployed SQLite data is ephemeral.
- Shared security-header and checker contributions include Student 5's #195.
  This report does not reattribute those changes to Student 1.

## Commit logs and use in the final report

The [commit-log table](student-1-release-2-commit-log.md) lists **31 original
commits across nine Student 1 Release 2 PRs**, with exact subjects, dates,
commit links and PR references. A separate table identifies each PR's merge
status and main integration SHA. Open work is not labelled merged or deployed.
That table remains the **08:42 UTC snapshot on 27 October**, before PRs #189
and #186 were merged; this cloud-only update does not rewrite that historical log.

For the group PDF, use the two report-ready text sections above, suitable
figures/captions, the run URLs and selected rows from the contribution table.
Link the full raw reports and commit table for the supporting detail. No
deployment approval or final team decision is created by this evidence pack.

## Capture provenance

[capture-manifest.json](student-1-report-evidence/capture-manifest.json)
records the original pack's capture time, source runs, screenshot types,
file sizes and SHA-256 hashes, including its retained historical cloud files.
The [27 October deployment manifest](https://github.com/YourNightmareIsOver/TripGenie/blob/2ff5baa43178189cf8bf5aada0b228bb993ff66a/docs/reports/release-2/cloud-evidence/2026-10-27/capture-manifest.json)
covers the newer linked cloud evidence. These sources are reused without
duplicating or altering them. A directory-scoped `.gitattributes` disables newline conversion
so the original artifact bytes and hashes survive checkout on other platforms.
The screenshots were made with real Chrome through Playwright.
The public GitHub run pages were captured without DOM editing. The full
artifact screenshots were rendered from the downloaded Markdown through
GitHub's Markdown renderer and a locally styled document, explicitly labelled
as rendered copies. No test result, report row or decision was invented.
