from github_mcp.create_file import create_file


def main():
    try:

        # Change these values to match your GitHub account
        owner = "manaswitha7"
        repo_name = "awos-mcp-test-20260706185050"

        file_path = "README.md"

        content = """# AWOS MCP Test

This README was created automatically using the AWOS GitHub MCP Server.

## Features

- GitHub MCP
- FastMCP
- Repository Automation

Generated for testing.
"""

        result = create_file(
            owner=owner,
            repo_name=repo_name,
            file_path=file_path,
            content=content,
            commit_message="Create README using AWOS MCP"
        )

        print("=" * 60)
        print("GitHub File Creation Test")
        print("=" * 60)

        print(f"Status      : {result.get('status')}")
        print(f"Message     : {result.get('message')}")

        if result.get("status") == "success":

            print(f"File Path   : {result.get('path')}")
            print(f"Blob SHA    : {result.get('sha')}")
            print(f"Commit SHA  : {result.get('commit_sha')}")
            print(f"URL         : {result.get('url')}")

        elif result.get("status") == "exists":

            print(f"File Path   : {result.get('path')}")
            print(f"Blob SHA    : {result.get('sha')}")

        print("=" * 60)

    except Exception as e:

        print("❌ File Creation Test Failed")
        print(e)


if __name__ == "__main__":
    main()
