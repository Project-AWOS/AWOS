from github import GithubException
from github_mcp.auth import get_github_client


def create_repository(
    repo_name: str,
    description: str = "",
    private: bool = False,
    auto_init: bool = True,
):
    """
    Create a new GitHub repository.

    Args:
        repo_name (str): Repository name.
        description (str): Repository description.
        private (bool): Whether repository is private.
        auto_init (bool): Initialize with README.

    Returns:
        dict: Structured response.
    """

    try:
        github = get_github_client()
        user = github.get_user()

        # Check whether repository already exists
        try:
            existing = user.get_repo(repo_name)

            return {
                "status": "exists",
                "message": "Repository already exists.",
                "repository": existing.full_name,
                "url": existing.html_url,
            }

        except GithubException:
            # Repository doesn't exist; continue.
            pass

        # Create repository
        repo = user.create_repo(
            name=repo_name,
            description=description,
            private=private,
            auto_init=auto_init,
        )

        return {
            "status": "success",
            "message": "Repository created successfully.",
            "repository": repo.full_name,
            "name": repo.name,
            "url": repo.html_url,
            "private": repo.private,
            "default_branch": repo.default_branch,
        }

    except GithubException as e:
        return {
            "status": "error",
            "message": str(e),
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }
