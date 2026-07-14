from github_mcp.auth import get_github_client


def search_code(owner: str, repo_name: str, keyword: str, max_results: int = 5):
    """
    Search for a keyword inside a GitHub repository.

    Returns:
        - file path
        - GitHub URL
        - matching code snippet
    """

    github = get_github_client()

    repo = github.get_repo(f"{owner}/{repo_name}")

    matches = []

    def get_snippet(text: str, keyword: str, context: int = 2):
        """
        Returns a few lines around the matched keyword.
        """

        lines = text.splitlines()

        for i, line in enumerate(lines):

            if keyword.lower() in line.lower():

                start = max(0, i - context)
                end = min(len(lines), i + context + 1)

                return "\n".join(lines[start:end])

        return ""

    def traverse(path=""):

        nonlocal matches

        if len(matches) >= max_results:
            return

        contents = repo.get_contents(path)

        if not isinstance(contents, list):
            contents = [contents]

        for item in contents:

            if len(matches) >= max_results:
                break

            if item.type == "dir":

                traverse(item.path)

            elif item.name.endswith(
                (
                    ".py",
                    ".md",
                    ".txt",
                    ".yaml",
                    ".yml",
                    ".json",
                )
            ):

                try:

                    text = item.decoded_content.decode(
                        "utf-8",
                        errors="ignore",
                    )

                    if keyword.lower() in text.lower():

                        snippet = get_snippet(text, keyword)

                        matches.append(
                            {
                                "file": item.path,
                                "url": item.html_url,
                                "snippet": snippet,
                            }
                        )

                except Exception:
                    continue

    traverse()

    return {
        "status": "success",
        "repository": repo.full_name,
        "keyword": keyword,
        "count": len(matches),
        "matches": matches,
    }
