import markdown
from bs4 import BeautifulSoup


def clean_markdown(md_text: str) -> str:
    """
    Convert markdown to clean plain text.
    """

    html = markdown.markdown(md_text)

    soup = BeautifulSoup(html, "html.parser")

    return soup.get_text(separator="\n")
