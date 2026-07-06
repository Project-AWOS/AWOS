"""
=========================================================
Module      : parser.py

System      : AWOS

Component   : AI

Purpose
-------
Parses and validates responses returned
by Large Language Models.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

import json


def parse_json_response(response: str) -> dict:
    """
    Convert an LLM response into a Python dictionary.

    This function removes Markdown code fences
    before parsing JSON.
    """

    response = response.strip()

    # Remove Markdown JSON fences
    if response.startswith("```json"):
        response = response.replace("```json", "", 1)

    if response.startswith("```"):
        response = response.replace("```", "", 1)

    if response.endswith("```"):
        response = response[:-3]

    response = response.strip()

    return json.loads(response)