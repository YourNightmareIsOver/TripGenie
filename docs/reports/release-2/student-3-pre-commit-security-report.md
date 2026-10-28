# Student 3 pre-commit security testing report (Release 2)

Scope: Student 3's contribution (`student-3/**`, the Transport
service). The shared gate (`scripts/security/scan.py`, run by the `security`
pre-commit hook) always scans the whole repository, so this report records the
full-repository result and then the Student 3 paths within it.

## Tools and versions

| Tool | Version | What it checks |
| --- | --- | --- |
| Ruff | 0.16.5 | Every stable `S` (flake8-bandit) rule, using `scripts/security/ruff.toml` |
| detect-secrets | 1.5.0 | All detectors on every tracked or non-ignored file, with verification turned off |
| pip-audit | 2.10.0 | Runtime and optional dependencies from every `pyproject.toml` and `requirements*.txt` file, including transitive dependencies |

Environment: Python 3.11.15 on Linux. Scanned HEAD was `a9e7526` on `main`
(863 files, 29 dependency manifests, including the four Student 3
`pyproject.toml` files).

## Command run

```bash
.venv/bin/pre-commit run security --all-files -v
```

## Results

```text
ruff: passed
detect-secrets: failed
pip-audit: passed
Security gate: failed.
```

| Tool | Result | Student 3 paths |
| --- | --- | --- |
| Ruff | Passed: `All checks passed!` | No findings |
| pip-audit | Passed: 88 resolved dependencies, 0 known vulnerabilities | No findings |
| detect-secrets | Failed: 35 raw results, 27 not in `scripts/security/secret-allowlist.toml` | No findings |

## Findings

No finding is in Student 3's paths. Ruff and pip-audit are clean across the
repository, and none of the detect-secrets results are in `student-3/**`.

The gate fails only on detect-secrets results in another contribution's
Release 2 cloud evidence. All 27 are `Hex High Entropy String` results on
fingerprints, not credentials:

| File | Results | Flagged values |
| --- | --- | --- |
| `docs/reports/release-2/cloud-evidence/2026-10-27/capture-manifest.json` | 26 | 25 per-file `sha256` digests and the `deployed_sha` Git commit SHA |
| `docs/reports/release-2/cloud-evidence/2026-10-27/run-metadata.json` | 1 | The workflow run's `headSha` Git commit SHA |

The other 8 raw results are already allowlisted.

These evidence files are not Student 3's, so this report does not allowlist
them. The fix belongs with the cloud evidence: add each value to
`scripts/security/secret-allowlist.toml` with a reason, as the Graphify
checksums and Student 5 scan evidence already are. The hashes are left out of
this report on purpose, because raw hash values in a committed report would be
flagged by the same detectors.

## Not covered

This report covers only the pre-commit gate. It does not include a
blocked-commit demonstration or regression test results. Post-commit endpoint
testing is covered in `student-3-post-commit-testing-report.md`.
