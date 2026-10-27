# Student 1 Release 2 commit log

Snapshot: 27 October 2026. Scope: the nine Release 2 PRs authored by
`aadirai31` and opened between 19 and 23 October. This is a contribution
log, not the repository's complete history. Dates below are UTC.
Original commit subjects are copied from Git; they are not rewritten.
Public GitHub author/co-author attribution is retained in
[commit-provenance.json](student-1-report-evidence/commit-provenance.json).
Assistant co-authors remain credited in the linked commits.

## Contribution and merge status

| PR | Contribution | Status at capture | Main integration commit |
| --- | --- | --- | --- |
| [#179](https://github.com/YourNightmareIsOver/TripGenie/pull/179) | Release 2: Azure Container Apps deployment following Lab 11 (scripts + cloud-deployment.yml) | Merged | [`0736601`](https://github.com/YourNightmareIsOver/TripGenie/commit/073660101a8502f0ed564b24497f8138cf5be1bf) |
| [#180](https://github.com/YourNightmareIsOver/TripGenie/pull/180) | Release 2: make frontends cloud-ready and add the AI-off cloud profile (#167) | Merged | [`e89ec3d`](https://github.com/YourNightmareIsOver/TripGenie/commit/e89ec3d6aba877c2fde9a6557288d2b4b9a8b11b) |
| [#181](https://github.com/YourNightmareIsOver/TripGenie/pull/181) | Release 2: Student 1 post-commit endpoint tests in student-1-ci.yml (#174) | Merged | [`3ea4195`](https://github.com/YourNightmareIsOver/TripGenie/commit/3ea4195e490e7c4b6a5a3b67cec4302273b1d1e8) |
| [#182](https://github.com/YourNightmareIsOver/TripGenie/pull/182) | Release 2: Student 1 pre-commit security scan findings and report (#175) | Merged | [`d852c99`](https://github.com/YourNightmareIsOver/TripGenie/commit/d852c9915accd3852666e820e9df84e421497bc0) |
| [#186](https://github.com/YourNightmareIsOver/TripGenie/pull/186) | Release 2: draft cloud deployment report and architecture (#171) | Open | Not merged |
| [#187](https://github.com/YourNightmareIsOver/TripGenie/pull/187) | Release 2: cloud deployment prerequisites - registry pull identity with revision gate, canonical OIDC bootstrap, HTTPS behind ingress (#171) | Merged | [`188951a`](https://github.com/YourNightmareIsOver/TripGenie/commit/188951a5010ffedc68508ce5c4933b286441d376) |
| [#189](https://github.com/YourNightmareIsOver/TripGenie/pull/189) | Student 1: multi-agent "Plan my itinerary" (Release 2, refs #176) | Open | Not merged |
| [#190](https://github.com/YourNightmareIsOver/TripGenie/pull/190) | Student 1: hide AI panels when configuration switches them off | Merged | [`4ed8621`](https://github.com/YourNightmareIsOver/TripGenie/commit/4ed8621ec288684c0f37fdc6de0486491aa8164b) |
| [#201](https://github.com/YourNightmareIsOver/TripGenie/pull/201) | Add Student 1 Release 2 demonstration guide (provisional) | Open | Not merged |

## Original commits

| Committed (UTC) | Commit | PR | Kind | Commit subject |
| --- | --- | --- | --- | --- |
| 2026-10-19 09:24:26 | [`597eeff`](https://github.com/YourNightmareIsOver/TripGenie/commit/597eeff2d53d1e0c90d2a056a1c5ab3cada89244) | [#179](https://github.com/YourNightmareIsOver/TripGenie/pull/179) | Contribution | Release 2: Azure Container Apps deployment (Bicep, scripts, cloud-deployment.yml) |
| 2026-10-19 09:26:51 | [`45c0b2b`](https://github.com/YourNightmareIsOver/TripGenie/commit/45c0b2bbc43e3a8dd238d2faef2f21e0a3fab6e5) | [#180](https://github.com/YourNightmareIsOver/TripGenie/pull/180) | Contribution | Release 2: make frontends cloud-ready and add the AI-off cloud profile (#167) |
| 2026-10-19 09:33:24 | [`c830b8d`](https://github.com/YourNightmareIsOver/TripGenie/commit/c830b8db39266b764a6a73348a00031acca722da) | [#179](https://github.com/YourNightmareIsOver/TripGenie/pull/179) | Contribution | Bootstrap: GitHub signs in as a managed identity, not an app registration |
| 2026-10-19 10:41:45 | [`7179ba2`](https://github.com/YourNightmareIsOver/TripGenie/commit/7179ba2999181dbbc2ac60e04bcbbe9478a33f8c) | [#179](https://github.com/YourNightmareIsOver/TripGenie/pull/179) | Contribution | Follow ASD Lab 11's deployment scripts and workflow for Azure |
| 2026-10-20 21:12:04 | [`a84d645`](https://github.com/YourNightmareIsOver/TripGenie/commit/a84d64554d29d43c2ef519fc676c67b5fd29a02d) | [#179](https://github.com/YourNightmareIsOver/TripGenie/pull/179) | Contribution | Address review: narrow CI's Azure access, harden the deploy scripts |
| 2026-10-20 21:41:17 | [`8f515e2`](https://github.com/YourNightmareIsOver/TripGenie/commit/8f515e238818def8b4652f385d0c56319dc95520) | [#181](https://github.com/YourNightmareIsOver/TripGenie/pull/181) | Contribution | Add Student 1 post-commit endpoint tests to student-1-ci.yml (#174) |
| 2026-10-20 21:41:20 | [`ba051f9`](https://github.com/YourNightmareIsOver/TripGenie/commit/ba051f9eb0f8bfaffb393c5929705e517f088bcd) | [#182](https://github.com/YourNightmareIsOver/TripGenie/pull/182) | Contribution | Release 2: Student 1 pre-commit security scan report (#175) |
| 2026-10-20 21:51:03 | [`7bfd12f`](https://github.com/YourNightmareIsOver/TripGenie/commit/7bfd12f9cb3a9bb3467969018a26f40a24a0ba4e) | [#181](https://github.com/YourNightmareIsOver/TripGenie/pull/181) | Contribution | Link the PR CI run in the Student 1 post-commit testing report (#174) |
| 2026-10-21 08:30:20 | [`9c96eb6`](https://github.com/YourNightmareIsOver/TripGenie/commit/9c96eb6362e46847b88ffd1e5b94e54e21256152) | [#181](https://github.com/YourNightmareIsOver/TripGenie/pull/181) | Contribution | Fail Student 1 endpoint tests when the backend is unavailable (#174) |
| 2026-10-21 08:59:24 | [`06a4df4`](https://github.com/YourNightmareIsOver/TripGenie/commit/06a4df48d34d0f26ca9721ca580678dad4ece92a) | [#186](https://github.com/YourNightmareIsOver/TripGenie/pull/186) | Contribution | Release 2: draft cloud deployment report and architecture (#171) |
| 2026-10-21 09:00:25 | [`814d6a2`](https://github.com/YourNightmareIsOver/TripGenie/commit/814d6a23d66d3498de5bb98793be2b8138114601) | [#186](https://github.com/YourNightmareIsOver/TripGenie/pull/186) | Contribution | Record placeholder-revision cause and pending cloud fixes (#171) |
| 2026-10-21 09:06:09 | [`591c4fa`](https://github.com/YourNightmareIsOver/TripGenie/commit/591c4fa226d12bbae446c21a1ac3965002f276f4) | [#187](https://github.com/YourNightmareIsOver/TripGenie/pull/187) | Contribution | Release 2: trust Azure ingress forwarded headers on cloud frontends (#171) |
| 2026-10-21 09:06:09 | [`61aa77a`](https://github.com/YourNightmareIsOver/TripGenie/commit/61aa77aa615f6dc61e4795fddacef764213db406) | [#187](https://github.com/YourNightmareIsOver/TripGenie/pull/187) | Contribution | Release 2: pull images with a registry identity, gate deployments on revision readiness, and bootstrap the canonical OIDC subject (#171) |
| 2026-10-21 09:13:31 | [`952f9d3`](https://github.com/YourNightmareIsOver/TripGenie/commit/952f9d3a1e19ee4c8b175e207f9fd2bd5bd34533) | [#186](https://github.com/YourNightmareIsOver/TripGenie/pull/186) | Contribution | Link cloud prerequisite PR #187 in the cloud report draft |
| 2026-10-21 09:53:41 | [`0b3ec9e`](https://github.com/YourNightmareIsOver/TripGenie/commit/0b3ec9ef5d2c934583b5f1914124310d77c84a01) | [#189](https://github.com/YourNightmareIsOver/TripGenie/pull/189) | Contribution | Student 1: multi-agent "Plan my itinerary" (Release 2) |
| 2026-10-21 11:05:04 | [`88b06a2`](https://github.com/YourNightmareIsOver/TripGenie/commit/88b06a288a9788955f591c80e7f4301d9f99ea32) | [#186](https://github.com/YourNightmareIsOver/TripGenie/pull/186) | Merge synchronization | Merge main (#187) into cloud-report-draft |
| 2026-10-21 11:12:20 | [`d9b4309`](https://github.com/YourNightmareIsOver/TripGenie/commit/d9b430987f8d49f58deecefc4a180399811e1161) | [#190](https://github.com/YourNightmareIsOver/TripGenie/pull/190) | Contribution | Hide Student 1 AI panels when configuration switches them off |
| 2026-10-21 11:18:12 | [`af7de00`](https://github.com/YourNightmareIsOver/TripGenie/commit/af7de00be5203526a35e96435fb0eea2b6090ffd) | [#186](https://github.com/YourNightmareIsOver/TripGenie/pull/186) | Contribution | Record first cloud deployment run evidence in the cloud report draft |
| 2026-10-21 11:23:41 | [`05a78f3`](https://github.com/YourNightmareIsOver/TripGenie/commit/05a78f36fec884ff5e4e9cc30edda884c00f6aca) | [#186](https://github.com/YourNightmareIsOver/TripGenie/pull/186) | Contribution | Link pending Student 1 AI visibility PR #190 in the cloud report |
| 2026-10-22 23:57:02 | [`1599e81`](https://github.com/YourNightmareIsOver/TripGenie/commit/1599e815b1977b078ad0ceff61f5bf96dfcb48d9) | [#189](https://github.com/YourNightmareIsOver/TripGenie/pull/189) | Merge synchronization | Merge main into student-1-multi-agent |
| 2026-10-22 23:59:22 | [`c7e326d`](https://github.com/YourNightmareIsOver/TripGenie/commit/c7e326d6b77119afeb07d19a4395167c24a9d462) | [#189](https://github.com/YourNightmareIsOver/TripGenie/pull/189) | Contribution | Give the Student 1 planner's Planner and Reviewer the itinerary rules |
| 2026-10-23 00:06:05 | [`8e492fc`](https://github.com/YourNightmareIsOver/TripGenie/commit/8e492fc916351fc9dfccbe9abf63668d9ee4a6f3) | [#201](https://github.com/YourNightmareIsOver/TripGenie/pull/201) | Contribution | Add Student 1 Release 2 demonstration guide (refs #177) |
| 2026-10-23 00:12:35 | [`4b1fe3d`](https://github.com/YourNightmareIsOver/TripGenie/commit/4b1fe3d4f6cfb7850e98583fbb277e77e4bf9149) | [#201](https://github.com/YourNightmareIsOver/TripGenie/pull/201) | Contribution | Fix demo guide PowerShell commands, timing and review checklist (refs #177) |
| 2026-10-23 00:45:43 | [`63ecdc9`](https://github.com/YourNightmareIsOver/TripGenie/commit/63ecdc99e801bc2afabd50673b9606c84fc04c10) | [#189](https://github.com/YourNightmareIsOver/TripGenie/pull/189) | Contribution | Swap the whole shell after an HTMX AI suggestions request |
| 2026-10-23 01:20:22 | [`e13c752`](https://github.com/YourNightmareIsOver/TripGenie/commit/e13c75210d7202c1fdc53343524951debb811cf0) | [#201](https://github.com/YourNightmareIsOver/TripGenie/pull/201) | Contribution | Add verified cloud bonus-security demonstration segment |
| 2026-10-23 01:48:05 | [`0b17b43`](https://github.com/YourNightmareIsOver/TripGenie/commit/0b17b43d15e4edc6f612180309f06a4f379275cb) | [#201](https://github.com/YourNightmareIsOver/TripGenie/pull/201) | Contribution | Update demo guide with real Compose workflow evidence and recording profile |
| 2026-10-23 01:48:05 | [`651e7f8`](https://github.com/YourNightmareIsOver/TripGenie/commit/651e7f8ba57ba7cab60fd7271fb67dcd5361df69) | [#189](https://github.com/YourNightmareIsOver/TripGenie/pull/189) | Contribution | Document real Student 1 multi-agent decisions and small-GPU profile |
| 2026-10-23 01:54:31 | [`263b2cd`](https://github.com/YourNightmareIsOver/TripGenie/commit/263b2cd35204c4b5461bd0b457782cae7ba4eea2) | [#201](https://github.com/YourNightmareIsOver/TripGenie/pull/201) | Contribution | Link the demonstration guide to the planner prompt walkthrough |
| 2026-10-23 01:54:31 | [`a6b3ae0`](https://github.com/YourNightmareIsOver/TripGenie/commit/a6b3ae0e5a2a777c57125d07e935f09f8215a6ab) | [#189](https://github.com/YourNightmareIsOver/TripGenie/pull/189) | Contribution | Add planner prompts and four-decision recording walkthrough |
| 2026-10-23 01:59:36 | [`29239a1`](https://github.com/YourNightmareIsOver/TripGenie/commit/29239a10763950c8beeea6a80d0c4b327c0ce784) | [#189](https://github.com/YourNightmareIsOver/TripGenie/pull/189) | Contribution | Add cloud functionality and deployment evidence walkthrough to runbook |
| 2026-10-23 01:59:36 | [`d8b7f46`](https://github.com/YourNightmareIsOver/TripGenie/commit/d8b7f4681036b54842e5abaf9718eeb6a1c32225) | [#201](https://github.com/YourNightmareIsOver/TripGenie/pull/201) | Contribution | Link cloud recording steps and clarify host-only AI narration |

## Interpretation

- There are 31 original commits, including two branch-synchronization
  merges. Merge commits are not counted as new implementation work.
- The integration SHAs above identify merged PRs on `main`; original
  branch SHAs are retained so squash merges do not erase attribution.
- Open PRs #186, #189 and #201 are contributions awaiting merge, not
  evidence that their changes are deployed.
- The initial #179 commit mentions Bicep. Later commits replaced that
  approach with Lab 11-style scripts; the historical subject must not
  be read as a claim that the final deployment uses Bicep.
- This evidence-packaging PR is excluded from its own historical log
  to avoid a self-referencing commit. No earlier release contributions
  or teammates' PRs are attributed to Student 1 here.
