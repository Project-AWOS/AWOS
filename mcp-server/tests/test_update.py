from datetime import datetime

from github_mcp.update_file import update_file


def main():
    try:

        owner = "manaswitha7"
        repo_name = "awos-mcp-test-20260706185050"

        # Use the branch you created in test_create_branch.py
        branch = "feature-20260706190008"

        file_path = "README.md"

        new_content = f"""# AWOS MCP Test

README updated successfully.

Updated at:
{datetime.now()}

## Features

- GitHub MCP
- FastMCP
- Repository Automation
- Branch Management
- File Updates

This update was performed by test_update.py.
"""

        result = update_file(
            owner=owner,
            repo_name=repo_name,
            file_path=file_path,
            new_content=new_content,
            commit_message="Update README using AWOS MCP",
            branch=branch,
        )

        print("=" * 60)
        print("GitHub File Update Test")
        print("=" * 60)

        print(f"Status      : {result.get('status')}")
        print(f"Message     : {result.get('message')}")

        if result.get("status") == "success":

            print(f"File Path   : {result.get('path')}")
            print(f"Branch      : {result.get('branch')}")
            print(f"Blob SHA    : {result.get('sha')}")
            print(f"Commit SHA  : {result.get('commit_sha')}")
            print(f"URL         : {result.get('url')}")

        print("=" * 60)

    except Exception as e:

        print("❌ File Update Test Failed")
        print(e)


if __name__ == "__main__":
    main()
