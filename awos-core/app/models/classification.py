"""
=========================================================
Module      : classification.py

System      : AWOS

Component   : Models

Purpose
-------
Stores the classification produced by CORTEX.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

from pydantic import BaseModel


class MissionClassification(BaseModel):
    """
    Classification generated from a mission analysis.
    """

    domain: str

    category: str

    complexity: str