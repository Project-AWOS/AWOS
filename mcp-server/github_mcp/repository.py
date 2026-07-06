from github_mcp.auth import get_github_client


def get_repository(owner: str, repo_name: str):
    """
    Fetch detailed information about a GitHub repository.
    """

    github = get_github_client()

    repo = github.get_repo(f"{owner}/{repo_name}")

    return {
        "status": "success",
        "name": repo.full_name,
        "description": repo.description,
        "stars": repo.stargazers_count,
        "forks": repo.forks_count,
        "language": repo.language,
        "open_issues": repo.open_issues_count,
        "default_branch": repo.default_branch,
        "url": repo.html_url,
    }
