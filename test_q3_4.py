from question3 import get_repo_count

def test_empty_username_returns_zero():
    result = get_repo_count("")
    assert result == 0