# Student 2 pre-commit security testing report (Release 2)

Scope: Student 2's contribution (`student-2/**`). The shared gate
(`scripts/security/scan.py`, run by the `security` pre-commit hook) always
scans the whole repository, so this report records the full-repository result.

## Tools and versions

| Tool | Version | What it checks |
| --- | --- | --- |
| Ruff | 0.16.5 | Every stable `S` (flake8-bandit) rule, using `scripts/security/ruff.toml` |
| detect-secrets | 1.5.0 | All detectors on every tracked or non-ignored file, with verification turned off |
| pip-audit | 2.10.0 | Runtime and optional dependencies from every `pyproject.toml` and `requirements*.txt` file, including transitive dependencies |

Environment: Python 3.13 on macOS (darwin). Scanned HEAD was `d88c5dd`.

## Command run

```bash
.venv/bin/python scripts/security/scan.py
```

## Results

```text
ruff: passed
detect-secrets: passed
pip-audit: passed
Security gate: passed.
```

- Ruff printed `All checks passed!` with exit code 0.
- detect-secrets reported 0 new findings. The only raw results are the
  Graphify checksums in `graphify-out/`, which are already in
  `scripts/security/secret-allowlist.toml`.
- pip-audit found 0 vulnerabilities in the resolved dependencies.

## Findings

No open findings in Student 2's paths or elsewhere in the repository. No code
changes were needed.

## First attempt: failed, then fixed

The first scan of this branch failed in detect-secrets. The cause was a raw
JSON scan output that had been staged under `docs/reports/release-2/`. It
contained Git SHAs, file hashes and detect-secrets hash values, which the
high-entropy and secret-keyword detectors flagged in the report itself. The
JSON was removed from the commit and replaced by this written report, so the
gate passes with nothing to allowlist.

## Not covered

This report covers only the pre-commit gate. It does not include a blocked-commit
demonstration or regression test results.
