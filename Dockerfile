FROM python:3.10-slim

WORKDIR /app

# avoid running as root in container
RUN useradd -m appuser || true

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY README.md ./

ENV PYTHONPATH=/app/src
EXPOSE 8000

USER appuser
CMD ["uvicorn","polymath_ai.web:app","--host","0.0.0.0","--port","8000"]
