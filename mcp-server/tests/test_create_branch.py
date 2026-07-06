from datetime import datetime

from github_mcp.create_branch import create_branch


def main():
    try:

        owner = "manaswitha7"
        repo_name = "awos-mcp-test-20260706185050"

        # Generate a unique branch name
        new_branch = f"feature-{datetime.now().strftime('%Y%m%d%H%M%S')}"

        result = create_branch(
            owner=owner,
            repo_name=repo_name,
            new_branch=new_branch,
            source_branch="main",
        )

        print("=" * 60)
        print("GitHub Branch Creation Test")
        print("=" * 60)

        print(f"Status          : {result.get('status')}")
        print(f"Message         : {result.get('message')}")

        if result.get("status") == "success":

            print(f"Branch          : {result.get('branch')}")
            print(f"Source Branch   : {result.get('source_branch')}")
            print(f"Commit SHA      : {result.get('commit_sha')}")

        elif result.get("status") == "exists":

            print(f"Branch          : {result.get('branch')}")

        print("=" * 60)

    except Exception as e:

        print("❌ Branch Creation Test Failed")
        print(e)


if __name__ == "__main__":
    main()
