from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from .assistant import Assistant
from .code_assistant import generate_code, run_code
from .doc_reader import summarize_text
from .data_analysis import analyze_csv

app = FastAPI(title="Polymath AI")

class PromptIn(BaseModel):
    prompt: str
    temperature: Optional[float] = 0.2
    run: Optional[bool] = False

class TextIn(BaseModel):
    text: str
    temperature: Optional[float] = 0.2

class AnalyzeIn(BaseModel):
    path: Optional[str] = None


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask")
def ask(body: PromptIn):
    a = Assistant()
    if not a.available:
        raise HTTPException(status_code=503, detail="OPENAI_API_KEY not configured on server")
    resp = a.respond(body.prompt, temperature=body.temperature)
    return {"response": resp}


@app.post("/generate_code")
def generate(body: PromptIn):
    # Allow code-generation endpoint to be tested even when OPENAI_API_KEY is unset.
    # Errors from the assistant are returned as HTTP 500 with the exception message.
    a = Assistant()
    try:
        code = generate_code(body.prompt, assistant=a)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    result = {"code": code}
    if body.run:
        rc, out, err = run_code(code)
        result.update({"exit_code": rc, "stdout": out, "stderr": err})
    return result


@app.post("/summarize")
def summarize(body: TextIn):
    a = Assistant()
    if not a.available:
        raise HTTPException(status_code=503, detail="OPENAI_API_KEY not configured on server")
    out = summarize_text(body.text, assistant=a, temperature=body.temperature)
    return {"summary": out}


@app.post("/analyze")
def analyze(body: AnalyzeIn):
    if not body.path:
        raise HTTPException(status_code=400, detail="Path to CSV required for server analyze endpoint (demo).")
    r = analyze_csv(body.path)
    return {"report": r}
