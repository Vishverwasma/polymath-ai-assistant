import os
from typing import Optional

try:
    from pypdf import PdfReader
except Exception:
    PdfReader = None


def extract_text_from_pdf(path: str) -> str:
    """Extract text from PDF using pypdf. Raises helpful error if pypdf missing."""
    if PdfReader is None:
        raise RuntimeError("pypdf not installed. Install with: pip install pypdf")
    reader = PdfReader(path)
    parts = []
    for p in reader.pages:
        parts.append(p.extract_text() or "")
    return "\n".join(parts)


def summarize_text(text: str, assistant=None, temperature: float = 0.2) -> str:
    """Summarize text using Assistant. Assistant will require OPENAI_API_KEY."""
    from .assistant import Assistant
    a = assistant or Assistant()
    prompt = (
        "Please provide a concise summary in bullets (5 or fewer) and a one-line TL;DR for the following text:\n\n" + text
    )
    return a.respond(prompt, temperature=temperature)
