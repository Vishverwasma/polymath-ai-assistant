import tempfile
import subprocess
import os
from typing import Tuple

from .assistant import Assistant


def generate_code(prompt: str, assistant: Assistant = None) -> str:
    """Ask the Assistant to generate a Python code snippet for the prompt."""
    a = assistant or Assistant()
    wrapper = (
        "You are a helpful assistant that outputs only valid Python 3 code.\n"
        "Focus on correctness and avoid side-effects.\n"
        "Respond with code only, without explanation.\n\n"
        f"Task:\n{prompt}\n"
    )
    return a.respond(wrapper)


def run_code(code: str, timeout: int = 5) -> Tuple[int, str, str]:
    """Run Python code in a temporary file with a timeout. Returns (exitcode, stdout, stderr).

    Runs with sys.executable, catches timeouts and exceptions, and cleans up the temp file.
    """
    import sys, traceback
    path = None
    try:
        with tempfile.NamedTemporaryFile('w', suffix='.py', delete=False) as fh:
            fh.write(code)
            path = fh.name
        proc = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=timeout)
        return proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired as e:
        return -1, e.stdout or "", (e.stderr or "") + "\nTimeoutExpired"
    except Exception as e:
        return -2, "", f"{e}\n" + traceback.format_exc()
    finally:
        if path and os.path.exists(path):
            try:
                os.unlink(path)
            except Exception:
                pass
