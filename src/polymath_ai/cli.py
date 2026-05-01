import typer
from polymath_ai.assistant import Assistant

app = typer.Typer()

@app.command()
def ask(prompt: str = typer.Option(..., "Prompt for the AI"), temperature: float = 0.2):
    """Send a prompt to the configured assistant and print the reply."""
    a = Assistant()
    try:
        resp = a.respond(prompt, temperature=temperature)
        typer.secho(resp, fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED)


@app.command()
def summarize(file: str = typer.Option(..., "Path to a text or PDF file"), temperature: float = 0.2):
    """Summarize a document (plain text or PDF) using the configured assistant."""
    from pathlib import Path
    from .doc_reader import extract_text_from_pdf, summarize_text

    p = Path(file)
    if not p.exists():
        typer.secho(f"File not found: {file}", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    text = ""
    if p.suffix.lower() == ".pdf":
        try:
            text = extract_text_from_pdf(str(p))
        except Exception as e:
            typer.secho(f"Could not extract PDF text: {e}", fg=typer.colors.RED)
            raise typer.Exit(code=1)
    else:
        text = p.read_text(encoding="utf-8")

    try:
        out = summarize_text(text, temperature=temperature)
        typer.secho(out, fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"Error summarizing: {e}", fg=typer.colors.RED)

@app.command()
def analyze(file: str = typer.Option(..., "Path to CSV file")):
    """Analyze a CSV file and print a brief report."""
    from pathlib import Path
    from .data_analysis import analyze_csv

    p = Path(file)
    if not p.exists():
        typer.secho(f"File not found: {file}", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    try:
        report = analyze_csv(str(p))
        typer.secho(str(report), fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"Error analyzing: {e}", fg=typer.colors.RED)


@app.command()
def code(prompt: str = typer.Option(None, "Prompt to generate code"), run: bool = typer.Option(False, "Whether to execute the generated code")):
    """Generate Python code for a prompt and optionally execute it (runs in a temporary process)."""
    from .code_assistant import generate_code, run_code
    if not prompt:
        typer.secho("Provide --prompt to generate code", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    try:
        code_text = generate_code(prompt)
        typer.secho("--- Generated code ---", fg=typer.colors.YELLOW)
        typer.secho(code_text, fg=typer.colors.GREEN)
        if run:
            typer.secho("--- Running code ---", fg=typer.colors.YELLOW)
            rc, out, err = run_code(code_text)
            typer.secho(f"Exit {rc}", fg=typer.colors.CYAN)
            if out:
                typer.secho(out, fg=typer.colors.GREEN)
            if err:
                typer.secho(err, fg=typer.colors.RED)
    except Exception as e:
        typer.secho(f"Error generating or running code: {e}", fg=typer.colors.RED)


if __name__ == "__main__":
    app()
