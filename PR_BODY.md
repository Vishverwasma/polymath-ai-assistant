Title: chore(ci): Hardening — CI, linting, Docker, Dependabot, security

Summary
This branch (hardening-ci-docker) adds project hardening: ruff + mypy linting, CI workflow, Dockerfile for local container verification, Dependabot config for weekly dependency updates, and a release workflow. Also added CONTRIBUTING, SECURITY, ISSUE and PR templates, and CHANGELOG.

Files changed
- .github/workflows/ci.yml
- pyproject.toml
- Dockerfile
- .github/dependabot.yml
- .github/workflows/release.yml
- CHANGELOG.md
- CONTRIBUTING.md, SECURITY.md, .github templates

Testing checklist
- [ ] Run unit tests: $env:PYTHONPATH=./src; pytest -q
- [ ] Run ruff: ruff check .
- [ ] Run mypy: mypy src
- [ ] Build Docker image locally: docker build -t polymath-ai .

Notes
Please review and merge to main when green. This branch is non-destructive and aims to catch issues early in CI.
