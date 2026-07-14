from github_mcp.readme import get_readme


def main():
    try:
        owner = "fastapi"
        repo_name = "fastapi"

        result = get_readme(owner, repo_name)

        print("=" * 60)
        print("Repository README")
        print("=" * 60)
        print(f"Status : {result['status']}")
        print()

        if result["status"] == "success":
            print(result["content"][:2000])   # Print first 2000 characters
        else:
            print(result["message"])

        print("=" * 60)

    except Exception as e:
        print("❌ README Test Failed")
        print(e)


if __name__ == "__main__":
    main()
