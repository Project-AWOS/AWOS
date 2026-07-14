import anyio

from app.mcp.client import mcp_client


async def main():

    result = await mcp_client.call_tool(
        server="github",
        tool="search_repository",
        arguments={
            "query": "FastAPI authentication",
            "limit": 3,
        },
    )

    print(result)


if __name__ == "__main__":
    anyio.run(main)
