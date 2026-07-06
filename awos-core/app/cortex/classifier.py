"""
=========================================================
Module      : classifier.py

System      : AWOS

Component   : CORTEX

Purpose
-------
Classifies a mission into domain,
category and complexity.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

from app.models.analysis import MissionAnalysis
from app.models.classification import MissionClassification
from app.knowledge.domains import DOMAIN_KEYWORDS

def detect_domain(keywords: list[str]) -> str:
    """
    Detect the domain based on extracted keywords.
    """

    scores = {}

    for domain, domain_keywords in DOMAIN_KEYWORDS.items():

        score = 0

        for keyword in keywords:

            if keyword.lower() in domain_keywords:
                score += 1

        scores[domain] = score

    best_domain = max(scores, key=scores.get)

    if scores[best_domain] == 0:
        return "General"

    return best_domain

def detect_category(analysis: MissionAnalysis) -> str:
    """
    Detect the project category from the mission.
    """

    keywords = analysis.keywords

    if "fastapi" in keywords or "backend" in keywords:
        return "Web Application"

    if "docker" in keywords or "kubernetes" in keywords:
        return "DevOps"

    if "database" in keywords:
        return "Database"

    return "General Project"

def estimate_complexity(analysis: MissionAnalysis) -> str:
    """
    Estimate mission complexity.
    """

    words = analysis.word_count

    if words < 10:
        return "Low"

    if words <= 25:
        return "Medium"

    return "High"

def classify_mission(analysis: MissionAnalysis) -> MissionClassification:
    """
    Perform a complete mission classification.

    Parameters
    ----------
    analysis : MissionAnalysis
        Output from the Analyzer.

    Returns
    -------
    MissionClassification
        Structured mission classification.
    """

    return MissionClassification(
        domain=detect_domain(analysis.keywords),
        category=detect_category(analysis),
        complexity=estimate_complexity(analysis),
    )





if __name__ == "__main__":

    from app.cortex.analyzer import analyze_mission

    sample = (
        "Build a Hospital Appointment System using FastAPI. "
        "Add reminders for patients! "
        "Deploy it on Docker?"
    )

    analysis = analyze_mission(sample)

    classification = classify_mission(analysis)

    print("\n========== CLASSIFICATION ==========\n")

    print(classification.model_dump_json(indent=4))