from question2 import Rope

def test_add_correct_length():
    r1 = Rope(5.5)
    r2 = Rope(7)
    result = r1 + r2
    assert result == 12.5
