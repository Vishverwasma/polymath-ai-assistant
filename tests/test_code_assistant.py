from polymath_ai.code_assistant import run_code


def test_run_code_simple():
    code = "print(1+1)"
    rc, out, err = run_code(code, timeout=2)
    assert rc == 0
    assert out.strip() == '2'
    assert err == ''
