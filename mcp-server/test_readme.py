from github_mcp.readme import get_readme

result = get_readme(
    "tadata-org",
    "fastapi_mcp"
)

if result["status"] == "success":
    print(result["content"][:1000])      # First 1000 characters
else:
    print(result)
