import os
import pytest
from polymath_ai.assistant import Assistant

def test_no_api_key_raises():
    # ensure OPENAI_API_KEY is not set for this test
    os.environ.pop('OPENAI_API_KEY', None)
    a = Assistant()
    with pytest.raises(RuntimeError):
        a.respond('Hello')

# Additional unit tests can be added; mocking OpenAI calls is recommended for CI
