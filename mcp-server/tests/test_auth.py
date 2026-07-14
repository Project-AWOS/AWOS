from github_mcp.auth import get_github_client


def main():
    try:
        client = get_github_client()
        user = client.get_user()

        print("=" * 50)
        print("✅ GitHub Authentication Successful")
        print("=" * 50)
        print(f"Username : {user.login}")
        print(f"Name     : {user.name}")
        print(f"Profile  : {user.html_url}")
        print("=" * 50)

    except Exception as e:
        print("❌ Authentication Failed")
        print(e)


if __name__ == "__main__":
    main()
