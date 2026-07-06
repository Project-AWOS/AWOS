from mcp.server.fastmcp import FastMCP

from github_mcp.workflow import execute_github_research_mission
from github_mcp.search import search_repositories
from github_mcp.create_repo import create_repository
from github_mcp.create_file import create_file
from github_mcp.create_branch import create_branch
from github_mcp.update_file import update_file
from github_mcp.pull_request import create_pull_request


print("Starting AWOS GitHub MCP Server...")

mcp = FastMCP("AWOS GitHub MCP Server")


@mcp.tool()
def research_repository(query: str):
    """Execute the complete AWOS GitHub research workflow."""
    return execute_github_research_mission(query)


@mcp.tool()
def search_repository(query: str, limit: int = 5):
    """Search GitHub repositories."""
    return search_repositories(query, limit)


@mcp.tool()
def create_github_repository(
    repo_name: str,
    description: str = "",
    private: bool = False
):
    """Create a GitHub repository."""
    return create_repository(
        repo_name=repo_name,
        description=description,
        private=private
    )


@mcp.tool()
def create_repository_file(
    owner: str,
    repo_name: str,
    file_path: str,
    content: str,
    commit_message: str = "Create file",
    branch: str = "main",
):
    """
    Create a new file in a GitHub repository.
    """
    return create_file(
        owner=owner,
        repo_name=repo_name,
        file_path=file_path,
        content=content,
        commit_message=commit_message,
    )


@mcp.tool()
def create_repository_branch(
    owner: str,
    repo_name: str,
    branch_name: str,
    source_branch: str = "main",
):
    """
    Create a new branch in a GitHub repository.

    Args:
        owner: Repository owner
        repo_name: Repository name
        branch_name: Name of the new branch
        source_branch: Base branch (default: main)

    Returns:
        Dictionary containing branch creation status.
    """
    return create_branch(
        owner=owner,
        repo_name=repo_name,
        new_branch=branch_name,
        source_branch=source_branch,
    )


@mcp.tool()
def update_repository_file(
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
        owner: Repository owner
        repo_name: Repository name
        file_path: File path (e.g. README.md)
        new_content: Updated file content
        commit_message: Git commit message
        branch: Branch name

    Returns:
        Dictionary containing update status.
    """
    return update_file(
        owner=owner,
        repo_name=repo_name,
        file_path=file_path,
        new_content=new_content,
        commit_message=commit_message,
        branch=branch,
    )


@mcp.tool()
def create_repository_pull_request(
    owner: str,
    repo_name: str,
    title: str,
    body: str,
    head_branch: str,
    base_branch: str = "main",
):
    """
    Create a Pull Request in a GitHub repository.

    Args:
        owner: Repository owner
        repo_name: Repository name
        title: Pull Request title
        body: Pull Request description
        head_branch: Source branch
        base_branch: Target branch

    Returns:
        Dictionary containing Pull Request details.
    """

    return create_pull_request(
        owner=owner,
        repo_name=repo_name,
        title=title,
        body=body,
        head_branch=head_branch,
        base_branch=base_branch,
    )


@mcp.tool()
def server_info():
    """
    Returns information about the MCP server.
    """

    return {
        "server": "AWOS GitHub MCP Server",
        "version": "1.0",
        "transport": "STDIO",
        "tools": [
            "research_repository",
            "search_repository",
            "create_github_repository",
            "create_repository_file",
            "create_repository_branch",
            "update_repository_file",
            "create_repository_pull_request"
        ]
    }


print("Server initialized. Waiting for MCP client...")

if __name__ == "__main__":
    mcp.run()
