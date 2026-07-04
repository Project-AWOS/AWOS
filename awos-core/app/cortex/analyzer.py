"""
=========================================================
Module      : analyzer.py

System      : AWOS

Component   : CORTEX

Purpose
-------
Analyzes incoming mission text and extracts
basic linguistic information.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

import re
import string
from typing import Dict, List
from app.models.analysis import MissionAnalysis

# =========================================================
# Common words that are ignored while extracting keywords.
# =========================================================

STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "has",
    "have",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "to",
    "using",
    "with",
    "will",
}

# =========================================================
# Helper Functions
# =========================================================

def normalize_text(text: str) -> str:
    """
    Normalize mission text.

    This function:
    - Converts text to lowercase.
    - Removes punctuation.
    - Removes extra spaces.

    Parameters
    ----------
    text : str
        Original mission text.

    Returns
    -------
    str
        Cleaned mission text.
    """

    # Convert everything to lowercase
    text = text.lower()

    # Remove punctuation characters
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text

def count_words(text: str) -> int:
    """
    Count the number of words in the mission.

    Parameters
    ----------
    text : str
        Normalized mission text.

    Returns
    -------
    int
        Total number of words.
    """

    words = text.split()

    return len(words)

def count_sentences(text: str) -> int:
    """
    Count the number of sentences in the mission.

    Parameters
    ----------
    text : str
        Original mission text.

    Returns
    -------
    int
        Number of detected sentences.
    """

    # Split whenever we find ., ! or ?
    sentences = re.split(r"[.!?]+", text)

    # Remove empty results
    sentences = [s for s in sentences if s.strip()]

    return len(sentences)

def extract_keywords(text: str) -> List[str]:
    """
    Extract meaningful keywords from normalized text.

    Parameters
    ----------
    text : str
        Normalized mission text.

    Returns
    -------
    List[str]
        List of important keywords.
    """

    # Split text into individual words
    words = text.split()

    keywords = []

    for word in words:

        # Ignore stop words
        if word in STOP_WORDS:
            continue

        # Ignore numbers
        if word.isdigit():
            continue

        # Ignore very short words
        if len(word) <= 2:
            continue

        keywords.append(word)

    # Remove duplicates while preserving order
    unique_keywords = list(dict.fromkeys(keywords))

    return unique_keywords

def analyze_mission(text: str) -> MissionAnalysis:
    """
    Perform a complete mission analysis.

    Parameters
    ----------
    text : str
        Original mission description.

    Returns
    -------
    MissionAnalysis
        Structured analysis of the mission.
    """

    normalized = normalize_text(text)

    return MissionAnalysis(
        original_text=text,
        normalized_text=normalized,
        word_count=count_words(normalized),
        sentence_count=count_sentences(text),
        keywords=extract_keywords(normalized),
    )


if __name__ == "__main__":

    sample = (
        "Build a Hospital Appointment System using FastAPI. "
        "Add reminders for patients! "
        "Deploy it on Docker?"
    )

    analysis = analyze_mission(sample)

    print("\n========== MISSION ANALYSIS ==========\n")

    print(analysis.model_dump_json(indent=4))


