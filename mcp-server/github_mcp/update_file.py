from github import GithubException
from github_mcp.auth import get_github_client


def update_file(
    owner: str,
    repo_name: str,
    file_path: str,
    new_content: str,
    commit_message: str = "Update file",
    branch: str = "main",
):
    """
    Update an existing file in a GitHub repository.

    Args:
        owner: GitHub username or organization
        repo_name: Repository name
        file_path: File to update (e.g. README.md)
        new_content: Updated file content
        commit_message: Commit message
        branch: Branch to update

    Returns:
        dict
    """

    try:
        github = get_github_client()

        repo = github.get_repo(f"{owner}/{repo_name}")

        try:
            file = repo.get_contents(file_path, ref=branch)

        except GithubException:
            return {
                "status": "error",
                "message": f"File '{file_path}' not found in branch '{branch}'."
            }

        result = repo.update_file(
            path=file.path,
            message=commit_message,
            content=new_content,
            sha=file.sha,
            branch=branch,
        )

        return {
            "status": "success",
            "message": "File updated successfully.",
            "path": result["content"].path,
            "branch": branch,
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
