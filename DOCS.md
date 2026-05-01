Polymath AI — Developer docs

This project includes:
- src/polymath_ai: core modules
- tests/: unit tests using pytest
- examples/: demo curl commands and static HTML
- .github/workflows: simple CI that runs tests on push

Development
- Create virtualenv, install requirements, run pytest
- To run web server: uvicorn polymath_ai.web:app --reload

Security
- Code execution endpoint should only be used in a secure, local environment.
- When running in CI or servers, disable run capability or sandbox it in containers.
