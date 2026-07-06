from github_mcp.repository import get_repository

repo = get_repository(
    "tadata-org",
    "fastapi_mcp"
)

print(repo)
