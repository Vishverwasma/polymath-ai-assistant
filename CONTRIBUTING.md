Contributing

Thanks for contributing! Recommended workflow:

1. Fork the repo and create a branch from main (e.g. `hardening-ci-docker`).
2. Create small PRs with clear descriptions. Use the provided PR template.
3. Run tests and linters locally before pushing:
   - python -m venv .venv
   - .venv\Scripts\activate  # Windows
   - pip install -r requirements.txt
   - pip install ruff mypy
   - $env:PYTHONPATH=./src; pytest -q
   - ruff check .
   - mypy src || true
4. Security: do not enable POLYMATH_ALLOW_CODE_EXECUTION on public or CI runners.

Pushing and creating PRs (example):
   git checkout -b feature/your-change
   git add .
   git commit -m "feat: your change"
   git push origin feature/your-change
   Create PR on GitHub targeting main

If you need help, open an issue describing the problem and steps taken.
