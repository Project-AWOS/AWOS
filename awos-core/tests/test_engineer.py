import anyio

from app.agents.engineer import EngineerAgent


async def main():

    agent = EngineerAgent()

    result = await agent.execute(
        "Build FastAPI authentication service"
    )

    print(result.model_dump())


if __name__ == "__main__":
    anyio.run(main)
