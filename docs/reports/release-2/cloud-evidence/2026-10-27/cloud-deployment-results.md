# TripGenie Cloud Deployment Report

## Azure Container Apps

Deployment Status: Success

Resource Group: rg-tripgenie

Image Tag: 7bcedc9860cabbf4f1ab378c368102c36a1c9be2

Frontend URLs:

- https://shared-ui.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io
- https://student-1-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io
- https://student-2-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io
- https://student-3-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io
- https://student-4-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io
- https://student-5-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io

Validation Results:

| Check | Result | HTTP |
| --- | --- | --- |
| GET https://shared-ui.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 200 |
| GET https://student-1-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 200 |
| GET https://student-2-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 200 |
| GET https://student-3-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 200 |
| GET https://student-4-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 200 |
| GET https://student-5-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 200 |
| Create trip (POST /trips) | pass | 303 |
| Read trip (GET /trips/{id}) | pass | 200 |
| RAG disabled in the cloud | pass | 503 |
| Delete trip (POST /trips/{id}/delete) | pass | 303 |
| Trip gone after delete | pass | 404 |
| Security headers on https://shared-ui.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 200 |
| Server software hidden on https://shared-ui.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | nginx |
| HTTP redirects to HTTPS on shared-ui.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 301 |
| Security headers on https://student-1-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 200 |
| Server software hidden on https://student-1-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass |  |
| HTTP redirects to HTTPS on student-1-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 301 |
| Security headers on https://student-2-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 200 |
| Server software hidden on https://student-2-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass |  |
| HTTP redirects to HTTPS on student-2-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 301 |
| Security headers on https://student-3-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 200 |
| Server software hidden on https://student-3-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass |  |
| HTTP redirects to HTTPS on student-3-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 301 |
| Security headers on https://student-4-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 200 |
| Server software hidden on https://student-4-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass |  |
| HTTP redirects to HTTPS on student-4-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 301 |
| Security headers on https://student-5-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 200 |
| Server software hidden on https://student-5-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass |  |
| HTTP redirects to HTTPS on student-5-frontend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 301 |
| Not public: shared-backend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 404 |
| Not public: shared-database.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 404 |
| Not public: student-1-backend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 404 |
| Not public: student-1-database.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 404 |
| Not public: student-2-backend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 404 |
| Not public: student-2-database.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 404 |
| Not public: student-3-backend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 404 |
| Not public: student-3-database.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 404 |
| Not public: student-4-backend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 404 |
| Not public: student-4-database.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 404 |
| Not public: student-5-backend.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 404 |
| Not public: student-5-database.lemonrock-5a94d8cd.australiaeast.azurecontainerapps.io | pass | 404 |

Security Configuration:

| Check | Result | Detail |
| --- | --- | --- |
| Only shared-ui and the frontends are public | pass | 6 public |
| Public apps redirect HTTP to HTTPS | pass | none |
| Images pulled with a managed identity | pass | none |
| No credentials in plain app settings | pass | none |
| Registry admin user disabled | pass | False |
| Registry anonymous pull disabled | pass | False |

AI-Mode, MCP, RAG and the Multi-Agent Server are not deployed; the cloud
profile (shared/configuration/.env.cloud) turns every AI feature off.

Timestamp: 2026-10-27T09:02:57Z

Reviewer Notes: (pending agentic-loop Cloud Deployment Review)
