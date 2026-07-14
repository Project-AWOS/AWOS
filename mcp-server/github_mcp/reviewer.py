"""
reviewer.py

AWOS GitHub Mission Reviewer

Acts as the QA Agent.
Reviews GitHub operations before the final approval.
"""

from typing import Dict, List


def review_mission(
    execution_plan: Dict,
    github_results: Dict
) -> Dict:
    """
    Review the execution results.

    Parameters
    ----------
    execution_plan : dict
        Output from planner.py

    github_results : dict
        Results returned by workflow.py

    Returns
    -------
    dict
    """

    issues: List[str] = []
    passed_checks: List[str] = []

    quality_score = 10

    # ----------------------------
    # Repository Check
    # ----------------------------
    if github_results.get("repository"):

        passed_checks.append(
            "Repository successfully identified."
        )

    else:

        issues.append(
            "Repository information missing."
        )

        quality_score -= 2

    # ----------------------------
    # Documentation Check
    # ----------------------------
    documentation = github_results.get(
        "documentation",
        ""
    )

    if documentation and documentation != "README not available.":

        passed_checks.append(
            "README documentation available."
        )

    else:

        issues.append(
            "README documentation missing."
        )

        quality_score -= 2

    # ----------------------------
    # Recommendation Check
    # ----------------------------
    recommendation = github_results.get(
        "recommendation"
    )

    if recommendation:

        passed_checks.append(
            "Repository recommendation generated."
        )

    else:

        issues.append(
            "Recommendation missing."
        )

        quality_score -= 2

    # ----------------------------
    # Implementation Examples
    # ----------------------------
    examples = github_results.get(
        "implementation_examples",
        []
    )

    if len(examples) > 0:

        passed_checks.append(
            f"{len(examples)} implementation example(s) found."
        )

    else:

        issues.append(
            "No implementation examples found."
        )

        quality_score -= 1

    # ----------------------------
    # Risk Analysis
    # ----------------------------
    if github_results.get("risk_analysis"):

        passed_checks.append(
            "Risk analysis completed."
        )

    else:

        issues.append(
            "Risk analysis missing."
        )

        quality_score -= 1

    # ----------------------------
    # Mission Status
    # ----------------------------
    if quality_score >= 9:

        verdict = "Approved"

    elif quality_score >= 7:

        verdict = "Approved with Suggestions"

    else:

        verdict = "Needs Review"

    return {

        "status": "success",

        "qa_verdict": verdict,

        "quality_score": quality_score,

        "issues_found": issues,

        "checks_passed": passed_checks,

        "approval_required": True,

        "review_summary": (
            f"Mission completed with quality score "
            f"{quality_score}/10."
        )

    }


if __name__ == "__main__":

    sample_results = {

        "repository": "fastapi-users/fastapi-users",

        "documentation": "README content",

        "recommendation": {

            "level": "Highly Recommended"

        },

        "implementation_examples": [

            "example1.py"

        ],

        "risk_analysis": {

            "overall_risk": "Low"

        }

    }

    sample_plan = {

        "mission_type": "research"

    }

    from pprint import pprint

    pprint(
        review_mission(
            sample_plan,
            sample_results
        )
    )
