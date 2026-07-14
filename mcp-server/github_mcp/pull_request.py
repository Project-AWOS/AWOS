from github import GithubException
from github_mcp.auth import get_github_client


def create_pull_request(
    owner: str,
    repo_name: str,
    title: str,
    body: str,
    head_branch: str,
    base_branch: str = "main",
):
    """
    Create a Pull Request.

    Args:
        owner: GitHub username or organization
        repo_name: Repository name
        title: Pull Request title
        body: Pull Request description
        head_branch: Source branch
        base_branch: Target branch

    Returns:
        dict
    """

    try:
        github = get_github_client()

        repo = github.get_repo(f"{owner}/{repo_name}")

        # Check if an open PR already exists
        pulls = repo.get_pulls(state="open")

        for pr in pulls:
            if (
                pr.head.ref == head_branch
                and pr.base.ref == base_branch
            ):
                return {
                    "status": "exists",
                    "message": "Pull Request already exists.",
                    "pull_request": pr.title,
                    "url": pr.html_url,
                    "number": pr.number,
                }

        # Create Pull Request
        pr = repo.create_pull(
            title=title,
            body=body,
            head=head_branch,
            base=base_branch,
        )

        return {
            "status": "success",
            "message": "Pull Request created successfully.",
            "number": pr.number,
            "title": pr.title,
            "url": pr.html_url,
            "state": pr.state,
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
