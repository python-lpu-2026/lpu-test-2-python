"""
Question 3: Fetch Public Repository Count of a GitHub User (30 Marks)

Problem Description:
GitHub provides a public REST API that allows developers to fetch information about users.

Write a Python function that:
- Accepts a GitHub username as input
- Makes an HTTP GET request to the GitHub REST API
- Reads the JSON response
- Returns the number of public repositories for that user

API Endpoint: https://api.github.com/users/{username}

Implement the below function - get_repo_count()
Input:
username (string): GitHub username

Output:
- Integer representing number of public repositories
- Return 0 if user does not exist or request fails

Constraints:
- Use HTTP GET method only
- No authentication token required
- Function must not crash
- Always return an integer

Evaluation Rubric (30 Marks):
- Correct API endpoint usage -> 8 marks
- HTTP request implementation -> 4 marks
- JSON parsing -> 4 marks
- Error handling -> 4 marks
- Code logic and readability -> 10 marks

"""

def get_repo_count(username):
    """
    Returns the number of public repositories of a GitHub user.
    """
    pass