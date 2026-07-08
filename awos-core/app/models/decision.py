from pydantic import BaseModel


class AgentDecision(BaseModel):
    summary: str

    use_research: bool
    use_engineer: bool
    use_qa: bool

    requires_approval: bool

    tools: list[str]