import anyio

from app.mcp.manager import mcp_manager


async def main():

    query = input("GitHub Search Query: ")

    result = await mcp_manager.call(
        server="github",
        tool="search_repository",
        arguments={
            "query": query,
            "limit": 5,
        },
    )

    print(result)


if __name__ == "__main__":
    anyio.run(main)
