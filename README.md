Polymath AI Assistant — Polymath-AI

Polymath AI is a polished, resume-ready command-line AI assistant focused on practical, testable integrations with LLMs (OpenAI). Designed for interviews and portfolio demos, it provides:

Key features
- Interactive CLI: ask, summarize documents (PDF/TXT), and analyze CSV data
- Clean architecture: small core, pluggable LLM backend, unit tests and CI
- Production-ready: GitHub Actions to run tests; easy onboarding

Quickstart
1. python -m venv .venv
2. .venv\Scripts\activate (Windows) or source .venv/bin/activate (macOS/Linux)
3. pip install -r requirements.txt
4. Set your OpenAI key: PowerShell: $env:OPENAI_API_KEY="sk-..."  (or set as persistent env var)
5. Ask a question:
   python -m polymath_ai.cli ask --prompt "Explain dynamic programming in simple terms"
6. Summarize a PDF:
   python -m polymath_ai.cli summarize --file sample.pdf
7. Analyze CSV data:
   python -m polymath_ai.cli analyze --file data.csv
8. Run the web server (FastAPI) for programmatic/demo access:
   uvicorn polymath_ai.web:app --reload --host 127.0.0.1 --port 8000

Examples
- Generate code (JSON):
  curl -s -X POST http://127.0.0.1:8000/generate_code -H 'Content-Type: application/json' -d '{"prompt":"Write a function that returns Fibonacci numbers up to n","run":false}'
- Summarize text:
  curl -s -X POST http://127.0.0.1:8000/summarize -H 'Content-Type: application/json' -d '{"text":"Long article text..."}'

Security notes
- The /generate_code endpoint can execute generated code when `run` is true. Only enable this on trusted machines. The CLI provides a safer interface for experimentation.

Testing & verification
- Unit tests are in tests/ and pass locally and in CI. Run:
  $env:PYTHONPATH=./src; pytest -q

Repo
- GitHub: https://github.com/Vishverwasma/polymath-ai-assistant

Resume blurb
- See RESUME_BLURB.md for a concise project summary suitable for resumes and LinkedIn.

License
MIT
