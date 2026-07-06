from datetime import datetime

from github_mcp.create_repo import create_repository


def main():
    try:
        # Generate a unique repository name
        repo_name = f"awos-mcp-test-{datetime.now().strftime('%Y%m%d%H%M%S')}"

        result = create_repository(
            repo_name=repo_name,
            description="AWOS MCP Test Repository",
            private=True
        )

        print("=" * 60)
        print("GitHub Repository Creation Test")
        print("=" * 60)

        print(f"Status      : {result.get('status')}")
        print(f"Message     : {result.get('message')}")

        if result.get("status") in ["success", "exists"]:
            print(f"Repository  : {result.get('repository')}")
            print(f"Name        : {result.get('name', 'N/A')}")
            print(f"URL         : {result.get('url')}")
            print(f"Private     : {result.get('private', 'N/A')}")
            print(f"Branch      : {result.get('default_branch', 'N/A')}")

        print("=" * 60)

    except Exception as e:
        print("❌ Repository Creation Test Failed")
        print(e)


if __name__ == "__main__":
    main()
