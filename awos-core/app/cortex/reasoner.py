"""
=========================================================
Module      : reasoner.py

System      : AWOS

Component   : CORTEX

Purpose
-------
Uses Gemini to determine how a mission
should be executed.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

from app.ai.parser import parse_json_response

from app.ai.gemini import GeminiClient
from app.ai.prompts.reasoner import build_reasoner_prompt

from app.models.analysis import MissionAnalysis
from app.models.classification import MissionClassification
from app.models.reasoning import MissionReasoning


class MissionReasoner:
    """
    AI-powered reasoning engine.

    Converts mission analysis into
    structured execution reasoning.
    """

    def __init__(self):

        self.client = GeminiClient()

    def reason(
        self,
        analysis: MissionAnalysis,
        classification: MissionClassification,
    ) -> MissionReasoning:
        """
        Generate mission reasoning.
        """

        prompt = build_reasoner_prompt(
            analysis,
            classification,
        )

        response = self.client.generate(prompt)

        data = parse_json_response(response)

        return MissionReasoning(**data)