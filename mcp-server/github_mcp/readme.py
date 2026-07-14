from github_mcp.auth import get_github_client
from github_mcp.utils import clean_markdown


def get_readme(owner: str, repo_name: str):
    """
    Fetch the README content of a GitHub repository.
    """

    github = get_github_client()

    try:
        repo = github.get_repo(f"{owner}/{repo_name}")

        readme = repo.get_readme()

        content = clean_markdown(
            readme.decoded_content.decode("utf-8")
        )

        return {
            "status": "success",
            "repository": repo.full_name,
            "content": content
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
