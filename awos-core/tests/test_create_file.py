import anyio

from app.mcp.client import mcp_client


async def main():

    result = await mcp_client.call_tool(
        server="github",
        tool="create_repository_file",
        arguments={
            "owner": "manaswitha7",
            "repo_name": "awos-engineer-demo",
            "file_path": "README.md",
            "content": "# AWOS Engineer Demo\n\nCreated through AWOS MCP integration.",
            "commit_message": "Initial README",
            "branch": "feature/awos",
        },
    )

    print(result)


if __name__ == "__main__":
    anyio.run(main)
