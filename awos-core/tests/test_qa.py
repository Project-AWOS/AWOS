import anyio

from app.agents.qa import QAAgent


async def main():

    agent = QAAgent()

    result = await agent.execute()

    print(result.model_dump())


if __name__ == "__main__":
    anyio.run(main)
