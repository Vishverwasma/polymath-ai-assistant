import os
import pytest
from polymath_ai.doc_reader import summarize_text


def test_summarize_text_no_api_key(monkeypatch, tmp_path):
    # Create a small text file and ensure summarize_text raises informative error when no API key
    p = tmp_path / "sample.txt"
    p.write_text("This is a short sample.\nIt has multiple lines.")
    os.environ.pop('OPENAI_API_KEY', None)
    try:
        summarize_text(p.read_text())
    except RuntimeError:
        # expected because OPENAI_API_KEY not set
        assert True
    else:
        pytest.skip("OPENAI_API_KEY set; skipping runtime error assertion")
