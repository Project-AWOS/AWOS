"""
=========================================================
Module      : gemini.py

System      : AWOS

Component   : AI

Purpose
-------
Gemini implementation of the AIClient interface.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

import google.generativeai as genai

from app.ai.client import AIClient
from app.config.settings import settings


class GeminiClient(AIClient):
    """
    Gemini implementation of the AI client.
    """

    def __init__(self):

        print("Gemini key loaded:", bool(settings.GEMINI_API_KEY))
        print("Gemini key length:", len(settings.GEMINI_API_KEY))
        
        genai.configure(
            api_key=settings.GEMINI_API_KEY
        )

        self.model = genai.GenerativeModel(
            settings.GEMINI_MODEL
        )

    def generate(self, prompt: str) -> str:
        """
        Generate text using Gemini.
        """

        response = self.model.generate_content(prompt)

        return response.text