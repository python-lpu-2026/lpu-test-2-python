from question3 import get_repo_count

def test_valid_username_positive():
    result = get_repo_count("octocat")
    assert result > 0
