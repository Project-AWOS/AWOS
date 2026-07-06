from github_mcp.code_search import search_code

result = search_code(
    owner="tadata-org",
    repo_name="fastapi_mcp",
    keyword="authentication",
    max_results=5,
)

print("=" * 80)
print("Repository :", result["repository"])
print("Keyword    :", result["keyword"])
print("Matches    :", result["count"])
print("=" * 80)

for i, match in enumerate(result["matches"], start=1):

    print(f"\nMatch {i}")
    print("-" * 80)
    print("File    :", match["file"])
    print("URL     :", match["url"])
    print("\nSnippet:\n")
    print(match["snippet"])
    print("-" * 80)
