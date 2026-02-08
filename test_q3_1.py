from question3 import get_repo_count

def test_valid_username_returns_int():
    result = get_repo_count("octocat")
    assert isinstance(result, int)
