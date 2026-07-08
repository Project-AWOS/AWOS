import anyio

from app.agents.research import ResearchAgent


async def main():

    agent = ResearchAgent()

    result = await agent.execute(
        "FastAPI authentication"
    )

    print(result.model_dump())


if __name__ == "__main__":
    anyio.run(main)
