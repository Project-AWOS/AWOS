import anyio

from app.mcp.client import mcp_client


async def main():

    result = await mcp_client.call_tool(
        server="github",
        tool="create_repository_pull_request",
        arguments={
            "owner": "manaswitha7",
            "repo_name": "awos-engineer-demo",
            "title": "AWOS Initial Implementation",
            "body": "Created automatically through AWOS MCP integration.",
            "head_branch": "feature/awos",
            "base_branch": "main",
        },
    )

    print(result)


if __name__ == "__main__":
    anyio.run(main)
