"""
=========================================================
Module      : ceo.py

System      : AWOS

Component   : CEO Agent

Purpose
-------
Makes high-level execution decisions
for a mission.

Author
------
Project AWOS Team

Version
-------
Genesis v2.0
=========================================================
"""

from app.ai.gemini import GeminiClient
from app.ai.parser import parse_json_response
from app.ai.prompts.ceo import build_ceo_prompt

from app.models.analysis import MissionAnalysis
from app.models.classification import MissionClassification
from app.models.decision import AgentDecision


class CEOAgent:
    """
    Chief Executive Officer Agent.

    Uses Gemini for intelligent decision-making.
    Falls back to rule-based logic if Gemini fails.
    """

    def __init__(self):
        self.client = GeminiClient()

    def decide(
        self,
        analysis: MissionAnalysis,
        classification: MissionClassification,
    ) -> AgentDecision:

        try:

            prompt = build_ceo_prompt(
                analysis,
                classification,
            )

            response = self.client.generate(prompt)

            data = parse_json_response(response)

            return AgentDecision.model_validate(data)

        except Exception as e:

            print("\n========== CEO GEMINI FAILED ==========")
            print(e)
            print("Falling back to Rule-Based CEO.\n")

            return self.rule_based_decision(
                analysis,
                classification,
            )

    def rule_based_decision(
        self,
        analysis: MissionAnalysis,
        classification: MissionClassification,
    ) -> AgentDecision:

        mission = analysis.normalized_text.lower()

        use_research = False
        use_engineer = False
        use_qa = False

        tools = []

        reason = ""

        # --------------------------
        # Research missions
        # --------------------------

        if any(word in mission for word in [
            "research",
            "analyze",
            "study",
            "investigate",
            "search",
        ]):

            use_research = True
            tools.append("GitHub MCP")

            reason = "Mission requires research."

        # --------------------------
        # Engineering missions
        # --------------------------

        if any(word in mission for word in [
            "build",
            "develop",
            "implement",
            "create",
            "repository",
            "repo",
            "github",
            "code",
        ]):

            use_engineer = True

            if "GitHub MCP" not in tools:
                tools.append("GitHub MCP")

            if reason:
                reason += " Engineering is required."
            else:
                reason = "Mission requires engineering."

        # --------------------------
        # QA missions
        # --------------------------

        if any(word in mission for word in [
            "test",
            "validate",
            "review",
            "qa",
            "quality",
        ]):

            use_qa = True

            if "GitHub MCP" not in tools:
                tools.append("GitHub MCP")

            if reason:
                reason += " QA validation is required."
            else:
                reason = "Mission requires QA."

        # --------------------------
        # Full SDLC
        # --------------------------

        if (
            classification.category.lower() == "development"
            and classification.complexity.lower() in ["medium", "high"]
        ):

            use_research = True
            use_engineer = True
            use_qa = True

            if "GitHub MCP" not in tools:
                tools.append("GitHub MCP")

            reason = (
                "Complete software development lifecycle is required."
            )

        # --------------------------
        # Default
        # --------------------------

        if not (use_research or use_engineer or use_qa):

            use_research = True

            if "GitHub MCP" not in tools:
                tools.append("GitHub MCP")

            reason = (
                "Mission could not be classified precisely. "
                "Starting with Research."
            )

        return AgentDecision(
            summary="Mission approved by CEO.",

            use_research=use_research,
            use_engineer=use_engineer,
            use_qa=use_qa,

            requires_approval=False,

            tools=tools,

            reason=reason,
        )