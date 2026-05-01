import os
try:
    import openai
except Exception:
    openai = None

class Assistant:
    """Small wrapper around OpenAI ChatCompletion with sensible defaults.

    Usage: set OPENAI_API_KEY in environment and call Assistant().respond(prompt)
    """
    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.model = model
        key = os.getenv("OPENAI_API_KEY")
        if key:
            openai.api_key = key
            self.available = True
        else:
            self.available = False

    def respond(self, prompt: str, temperature: float = 0.2) -> str:
        """Return the model response for the given prompt."""
        if not self.available:
            raise RuntimeError("OPENAI_API_KEY not set. Export OPENAI_API_KEY to use the assistant.")
        resp = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=1200,
        )
        return resp.choices[0].message.content.strip()
