from mcp.server.fastmcp import FastMCP

from tools.github_tool import search_repo
from tools.filesystem_tool import write_file, read_file

mcp = FastMCP("AWOS MCP Server")


@mcp.tool()
def github_search(query: str):
    """
    Search GitHub repositories.
    """
    return search_repo(query)


@mcp.tool()
def save_report(filename: str, content: str):
    """
    Save report to workspace.
    """
    return write_file(filename, content)


@mcp.tool()
def load_report(filename: str):
    """
    Read report.
    """
    return read_file(filename)


if __name__ == "__main__":
    mcp.run()
