from github_mcp.code_search import search_code


def main():
    try:

        owner = "fastapi"
        repo_name = "fastapi"
        keyword = "APIRouter"

        result = search_code(
            owner=owner,
            repo_name=repo_name,
            keyword=keyword,
            max_results=5
        )

        print("=" * 60)
        print("GitHub Code Search")
        print("=" * 60)

        print(f"Repository : {result['repository']}")
        print(f"Keyword    : {result['keyword']}")
        print(f"Matches    : {result['count']}")

        print("=" * 60)

        if result["status"] == "success":

            for i, match in enumerate(result["matches"], start=1):

                print(f"{i}. File")

                print(f"   {match['file']}")

                print()

                print("Snippet")

                print(match["snippet"])

                print()

                print(f"URL : {match['url']}")

                print("-" * 60)

        else:

            print(result["message"])

    except Exception as e:

        print("❌ Code Search Test Failed")

        print(e)


if __name__ == "__main__":
    main()
