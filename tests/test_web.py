import pytest
from fastapi.testclient import TestClient
from polymath_ai import web

client = TestClient(web.app)


def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_generate_code_endpoint(monkeypatch):
    monkeypatch.setattr('polymath_ai.web.generate_code', lambda prompt, assistant=None: "print(42)")
    r = client.post('/generate_code', json={"prompt": "demo", "run": False})
    assert r.status_code == 200
    assert r.json()['code'].strip() == 'print(42)'


def test_analyze_endpoint(monkeypatch):
    monkeypatch.setattr('polymath_ai.web.analyze_csv', lambda path: {"rows": 2, "columns": 2})
    r = client.post('/analyze', json={"path": "dummy"})
    assert r.status_code == 200
    assert r.json()['report']['rows'] == 2
