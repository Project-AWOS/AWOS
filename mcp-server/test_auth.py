from github_mcp.auth import get_github_client

client = get_github_client()

user = client.get_user()

print(f"✅ Authenticated as: {user.login}")
