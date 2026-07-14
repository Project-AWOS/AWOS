"""
=========================================================
Module      : analysis.py

System      : AWOS

Component   : Models

Purpose
-------
Stores the structure of a mission analysis
produced by CORTEX.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

from pydantic import BaseModel
from typing import List


class MissionAnalysis(BaseModel):
    """
    Standard output produced by the CORTEX Analyzer.
    """

    original_text: str
    normalized_text: str

    word_count: int
    sentence_count: int

    keywords: List[str]