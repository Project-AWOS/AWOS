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
                "description": repo.description,
                "stars": repo.stargazers_count,
                "language": repo.language,
                "url": repo.html_url,
            }
        )

    return {
        "status": "success",
        "query": query,
        "count": len(results),
        "repositories": results,
    }
