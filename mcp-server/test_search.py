from github_mcp.search import search_repositories

result = search_repositories(
    "fastapi authentication",
    limit=5
)

print(result)
