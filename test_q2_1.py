from question2 import Rope

def test_add_returns_number():
    r1 = Rope(5)
    r2 = Rope(7)
    result = r1 + r2
    assert isinstance(result, (int, float))
