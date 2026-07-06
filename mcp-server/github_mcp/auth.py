import os
from dotenv import load_dotenv
from github import Github

# Load environment variables from .env
load_dotenv()


def get_github_client():
    """
    Returns an authenticated GitHub client.
    """
    token = os.getenv("GITHUB_TOKEN")

    if not token:
        raise ValueError("GITHUB_TOKEN not found in .env")

    return Github(token)
