from github import GithubException
from github_mcp.auth import get_github_client


def create_branch(
    owner: str,
    repo_name: str,
    new_branch: str,
    source_branch: str = "main",
):
    """
    Create a new branch from an existing branch.

    Args:
        owner: GitHub username
        repo_name: Repository name
        new_branch: Name of new branch
        source_branch: Base branch (default: main)

    Returns:
        dict
    """

    try:
        github = get_github_client()

        repo = github.get_repo(f"{owner}/{repo_name}")

        # Check if branch already exists
        try:
            existing = repo.get_branch(new_branch)

            return {
                "status": "exists",
                "message": "Branch already exists.",
                "branch": existing.name,
            }

        except GithubException:
            # Branch does not exist
            pass

        # Get source branch SHA
        source = repo.get_branch(source_branch)

        repo.create_git_ref(
            ref=f"refs/heads/{new_branch}",
            sha=source.commit.sha,
        )

        return {
            "status": "success",
            "message": "Branch created successfully.",
            "branch": new_branch,
            "source_branch": source_branch,
            "commit_sha": source.commit.sha,
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
