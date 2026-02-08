from question3 import get_repo_count

def test_invalid_username_returns_zero():
    result = get_repo_count("this_user_should_not_exist_12345")
    assert result == 0
