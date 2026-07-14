from github_mcp.pull_request import create_pull_request


def main():
    try:

        owner = "manaswitha7"
        repo_name = "awos-mcp-test-20260706185050"

        head_branch = "feature-20260706190008"
        base_branch = "main"

        title = "AWOS MCP Test Pull Request"

        body = """
## AWOS MCP Test

This Pull Request was created automatically by the AWOS GitHub MCP Server.

### Changes
- Updated README.md
- Tested GitHub MCP
- Ready for review

Generated automatically.
"""

        result = create_pull_request(
            owner=owner,
            repo_name=repo_name,
            title=title,
            body=body,
            head_branch=head_branch,
            base_branch=base_branch,
        )

        print("=" * 60)
        print("GitHub Pull Request Test")
        print("=" * 60)

        print(f"Status      : {result.get('status')}")
        print(f"Message     : {result.get('message')}")

        if result.get("status") == "success":

            print(f"PR Number   : {result.get('number')}")
            print(f"Title       : {result.get('title')}")
            print(f"State       : {result.get('state')}")
            print(f"URL         : {result.get('url')}")

        elif result.get("status") == "exists":

            print(f"PR Number   : {result.get('number')}")
            print(f"Title       : {result.get('pull_request')}")
            print(f"URL         : {result.get('url')}")

        print("=" * 60)

    except Exception as e:

        print("❌ Pull Request Test Failed")
        print(e)


if __name__ == "__main__":
    main()
