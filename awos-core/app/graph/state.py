from typing import TypedDict

from app.models.analysis import MissionAnalysis
from app.models.classification import MissionClassification
from app.models.reasoning import MissionReasoning
from app.models.planning import MissionPlan

from app.models.decision import AgentDecision

from app.agents.research import ResearchResult
from app.agents.engineer import EngineerResult
from app.agents.qa import QAResult
from app.agents.approval import ApprovalResult


class MissionState(TypedDict):

    mission: str

    analysis: MissionAnalysis | None

    classification: MissionClassification | None

    reasoning: MissionReasoning | None

    decision: AgentDecision | None

    research: ResearchResult | None

    engineering: EngineerResult | None

    qa: QAResult | None

    approval: ApprovalResult | None

    plan: MissionPlan | None