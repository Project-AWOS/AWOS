from github_mcp.auth import get_github_client


def search_repositories(query: str, limit: int = 5):
    """
    Search GitHub repositories and return the top results.
    """

    github = get_github_client()

    repositories = github.search_repositories(query=query)

    results = []

    for repo in repositories[:limit]:
        results.append(
            {
                "name": repo.full_name,
                "stars": repo.stargazers_count,
                "forks": repo.forks_count,
                "language": repo.language,
                "description": repo.description,
                "url": repo.html_url,
                "open_issues": repo.open_issues_count,
            }
        )

    return {
        "status": "success",
        "query": query,
        "count": len(results),
        "repositories": results,
    }
