from github import GithubException
from github_mcp.auth import get_github_client
import base64


def create_file(
    owner: str,
    repo_name: str,
    file_path: str,
    content: str,
    commit_message: str = "Create file",
):
    """
    Create a new file in a GitHub repository.

    Args:
        owner: GitHub username or organization.
        repo_name: Repository name.
        file_path: Path of the file (e.g. README.md).
        content: File contents.
        commit_message: Commit message.

    Returns:
        dict
    """

    try:
        github = get_github_client()

        repo = github.get_repo(f"{owner}/{repo_name}")

        # Check whether file already exists
        try:
            existing = repo.get_contents(file_path)

            return {
                "status": "exists",
                "message": "File already exists.",
                "path": existing.path,
                "sha": existing.sha,
            }

        except GithubException:
            # File does not exist
            pass

        result = repo.create_file(
            path=file_path,
            message=commit_message,
            content=content,
        )

        return {
            "status": "success",
            "message": "File created successfully.",
            "path": result["content"].path,
            "sha": result["content"].sha,
            "commit_sha": result["commit"].sha,
            "url": result["content"].html_url,
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
