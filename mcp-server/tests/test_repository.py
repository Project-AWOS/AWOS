from github_mcp.repository import get_repository


def main():
    try:
        owner = "fastapi"
        repo_name = "fastapi"

        result = get_repository(owner, repo_name)

        print("=" * 60)
        print("Repository Details")
        print("=" * 60)
        print(f"Name           : {result['name']}")
        print(f"Description    : {result['description']}")
        print(f"Stars          : {result['stars']}")
        print(f"Forks          : {result['forks']}")
        print(f"Language       : {result['language']}")
        print(f"Open Issues    : {result['open_issues']}")
        print(f"Default Branch : {result['default_branch']}")
        print(f"URL            : {result['url']}")
        print("=" * 60)

    except Exception as e:
        print("❌ Repository Test Failed")
        print(e)


if __name__ == "__main__":
    main()
