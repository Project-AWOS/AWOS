import anyio

from app.services.execution_service import execute_mission


async def main():

    result = await execute_mission(
        "Build a FastAPI authentication service"
    )

    print(result)


if __name__ == "__main__":
    anyio.run(main)
