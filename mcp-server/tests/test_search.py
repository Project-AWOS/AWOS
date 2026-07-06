from github_mcp.search import search_repositories


def main():
    try:
        query = "FastAPI authentication"

        result = search_repositories(query=query, limit=5)

        print("=" * 60)
        print("GitHub Repository Search")
        print("=" * 60)
        print(f"Query : {query}")
        print(f"Repositories Found : {result['count']}")
        print("=" * 60)

        for index, repo in enumerate(result["repositories"], start=1):
            print(f"{index}. {repo['name']}")
            print(f"   ⭐ Stars : {repo['stars']}")
            print(f"   🍴 Forks : {repo['forks']}")
            print(f"   💻 Language : {repo['language']}")
            print(f"   🔗 {repo['url']}")
            print()

    except Exception as e:
        print("❌ Search Test Failed")
        print(e)


if __name__ == "__main__":
    main()
