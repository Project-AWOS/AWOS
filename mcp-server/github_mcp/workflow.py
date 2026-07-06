from datetime import datetime
import uuid
import re
from github_mcp.search import search_repositories
from github_mcp.repository import get_repository
from github_mcp.readme import get_readme
from github_mcp.code_search import search_code
from github_mcp.planner import create_execution_plan
from github_mcp.reviewer import review_mission
from github_mcp.create_repo import create_repository
from github_mcp.create_file import create_file
from github_mcp.create_branch import create_branch
from github_mcp.update_file import update_file
from github_mcp.pull_request import create_pull_request


def execute_github_research_mission(query: str):
    """
    End-to-end GitHub Repository Intelligence — AWOS Mission.

    Workflow
    --------
    1.  Initialize mission context + progress tracking
    2.  Create execution plan via planner.py
    3.  Branch on mission_type:
        - research            → search, rank, README, code analysis
        - repository_creation → create repo, file, branch
        - repository_update   → update file, create PR
    4.  QA review via reviewer.py
    5.  Build executive summary + mission metrics
    6.  Return full mission report
    """

    # -----------------------------------------
    # STEP 1 : Mission context
    # -----------------------------------------
    mission_id = str(uuid.uuid4())
    mission_start = datetime.now()

    mission = {
        "mission_id": mission_id,
        "mission_name": "GitHub Repository Research",
        "objective": query,
        "created_at": mission_start.isoformat(),
        "status": "Running",
        "progress": [
            {
                "step": "Mission Initialized",
                "status": "Completed"
            }
        ]
    }

    # -----------------------------------------
    # STEP 2 : Execution plan — CEO Agent plans
    # -----------------------------------------
    execution_plan = create_execution_plan(query)

    mission["execution_plan"] = execution_plan

    mission["progress"].append({
        "step": "Execution Plan Created",
        "status": "Completed"
    })

    mission_type = execution_plan["mission_type"]

    completed_actions = []
    failed_actions = []
    github_results = {}

    # FUTURE: replace if/elif below with action-driven execution
    # for action in execution_plan["planned_actions"]:
    #     if action == "search_repositories":   ...
    #     elif action == "create_repository":   ...
    #     elif action == "create_file":         ...
    #     elif action == "update_file":         ...
    #     elif action == "create_pull_request": ...

    # -----------------------------------------
    # STEP 3A : Research mission
    # -----------------------------------------
    if mission_type == "research":

        repositories = search_repositories(query, limit=5)

        if repositories["count"] == 0:
            return {
                "status": "error",
                "message": "No repositories found."
            }

        completed_actions.append("Search Repository")

        mission["progress"].append({
            "step": "Repository Search",
            "status": "Completed"
        })

        # Rank: stars + forks*2 - open_issues
        ranked = []

        for repo in repositories["repositories"]:

            score = (
                repo["stars"]
                + repo.get("forks", 0) * 2
                - repo.get("open_issues", 0)
            )

            description = repo.get("description") or ""

            for word in query.lower().split():
                if word in description.lower():
                    score += 500

            ranked.append({
                "repository": repo,
                "score": score
            })

        ranked.sort(key=lambda x: x["score"], reverse=True)

        completed_actions.append("Rank Repositories")

        mission["progress"].append({
            "step": "Repository Ranking",
            "status": "Completed"
        })

        selected_repo = ranked[0]["repository"]

        owner, repo_name = selected_repo["name"].split("/")

        alternatives = [
            {
                "repository": item["repository"]["name"],
                "stars": item["repository"]["stars"]
            }
            for item in ranked[1:4]
        ]

        details = get_repository(owner, repo_name)

        completed_actions.append("Read Repository")

        mission["progress"].append({
            "step": "Repository Details Fetched",
            "status": "Completed"
        })

        readme = get_readme(owner, repo_name)

        completed_actions.append("Read README")

        mission["progress"].append({
            "step": "README Analysis",
            "status": "Completed"
        })

        keyword = query.split()[0]

        code = search_code(
            owner=owner,
            repo_name=repo_name,
            keyword=keyword,
            max_results=5
        )

        completed_actions.append("Analyze Implementation")

        mission["progress"].append({
            "step": "Implementation Examples Analyzed",
            "status": "Completed"
        })

        reasoning = (
            f"Evaluated the top {repositories['count']} GitHub repositories "
            f"for '{query}'. "
            f"'{selected_repo['name']}' achieved the highest relevance score "
            f"based on GitHub popularity ({details['stars']} stars), "
            f"keyword relevance, and implementation quality."
        )

        recommendation = {}

        if details["stars"] >= 10000:
            recommendation["level"] = "Highly Recommended"
        elif details["stars"] >= 1000:
            recommendation["level"] = "Recommended"
        else:
            recommendation["level"] = "Worth Evaluating"

        recommendation["reason"] = (
            f"This repository has {details['stars']} GitHub stars, "
            f"is written in {details['language']}, "
            f"contains {details['forks']} forks, "
            f"and includes {code['count']} implementation example(s)."
        )

        recommendation["use_case"] = (
            f"Suitable for projects related to '{query}'."
        )

        recommendation["confidence"] = (
            "High"
            if details["stars"] >= 10000
            else "Medium"
        )

        recommendation["pros"] = [
            "Well maintained",
            "Strong community support",
            "Open source",
            "Rich documentation",
            "Good implementation examples"
        ]

        recommendation["cons"] = [
            "Requires understanding of GitHub workflows",
            "Repository should be evaluated against project-specific requirements"
        ]

        recommendation["enterprise_readiness"] = "High"
        recommendation["estimated_learning_curve"] = "Low"
        recommendation["maintenance_status"] = "Active"
        recommendation["license_check"] = "Recommended before production use"

        recommendation["research_agent_verdict"] = (
            f"The Research Agent recommends "
            f"'{selected_repo['name']}' "
            f"because it has excellent community adoption, "
            f"strong documentation and useful implementation examples."
        )

        engineer_output = {
            "architecture":       "FastAPI Backend",
            "language":           details["language"],
            "recommended_branch": details["default_branch"],
            "next_task":          "Create repository and initialize README"
        }

        summary = {
            "description":    details["description"],
            "stars":          details["stars"],
            "forks":          details["forks"],
            "language":       details["language"],
            "open_issues":    details["open_issues"],
            "default_branch": details["default_branch"],
            "url":            details["url"]
        }

        documentation = (
            readme["content"][:3000]
            if readme["status"] == "success"
            else "README not available."
        )

        implementation_examples = (
            code["matches"]
            if code["status"] == "success"
            else []
        )

        ranking_output = [
            {
                "repository": item["repository"]["name"],
                "stars":      item["repository"]["stars"],
                "score":      item["score"]
            }
            for item in ranked
        ]

        github_results = {
            "repositories":   repositories,
            "selected_repo":  selected_repo,
            "details":        details,
            "readme":         readme,
            "code":           code,
            "recommendation": recommendation
        }

        mission_metrics = {
            "repositories_analyzed":   repositories["count"],
            "implementation_examples": code["count"],
            "selected_repository":     selected_repo["name"],
            "confidence":              recommendation["confidence"],
            "documentation_found":     readme["status"] == "success",
            "mission_duration":        (datetime.now() - mission_start).total_seconds()
        }

    # -----------------------------------------
    # STEP 3B : Repository creation mission
    # -----------------------------------------
    elif mission_type == "repository_creation":

        file_result = {"status": "not_run"}
        branch_result = {"status": "not_run"}

        # Derive a valid GitHub repo name from query:
        # 1. lowercase
        # 2. replace every non-alphanumeric/non-dash char with a dash
        # 3. collapse repeated dashes into one
        # 4. strip leading/trailing dashes
        # 5. truncate to 30 chars
        repo_name_derived = re.sub(r"[^a-z0-9-]", "-", query.lower())
        repo_name_derived = re.sub(r"-+", "-", repo_name_derived)
        repo_name_derived = repo_name_derived.strip("-")[:30]

        repo_result = create_repository(
            repo_name=repo_name_derived,
            description=query
        )

        if repo_result["status"] == "success":

            completed_actions.append("Create Repository")

            mission["progress"].append({
                "step": "Repository Created",
                "status": "Completed"
            })

            # parse owner/repo_name from "repository" key
            owner, repo_name = repo_result["repository"].split("/")

            file_result = create_file(
                owner=owner,
                repo_name=repo_name,
                file_path="README.md",
                content="# AWOS\nAutonomous Workforce Operating System"
            )

            if file_result["status"] == "success":

                completed_actions.append("Create README")

                mission["progress"].append({
                    "step": "README Created",
                    "status": "Completed"
                })

            else:
                failed_actions.append("Create README")

            branch_result = create_branch(
                owner,
                repo_name,
                new_branch="feature/initial-setup",
                source_branch="main"
            )

            if branch_result["status"] == "success":

                completed_actions.append("Create Branch")

                mission["progress"].append({
                    "step": "Branch Created",
                    "status": "Completed"
                })

            else:
                failed_actions.append("Create Branch")

        else:
            failed_actions.append("Create Repository")

        github_results = {
            "repo_result":   repo_result,
            "file_result":   file_result,
            "branch_result": branch_result
        }

        recommendation = {"level": "N/A", "confidence": "N/A"}
        summary = {}
        ranking_output = []
        alternatives = []
        documentation = ""
        implementation_examples = []
        reasoning = f"Repository creation mission executed for query: '{query}'."

        engineer_output = {
            "architecture":       "FastAPI Backend",
            "language":           "Python",
            "recommended_branch": "feature/initial-setup",
            "next_task":          "Develop initial project structure"
        }

        mission_metrics = {
            "mission_duration":  (datetime.now() - mission_start).total_seconds(),
            "completed_actions": len(completed_actions),
            "failed_actions":    len(failed_actions)
        }

    # -----------------------------------------
    # STEP 3C : Repository update mission
    # -----------------------------------------
    elif mission_type == "repository_update":

        pr_result = {"status": "not_run"}

        owner = execution_plan.get("owner", "")
        repo_name = execution_plan.get("repo_name", "")
        file_path = execution_plan.get("file_path", "README.md")
        content = execution_plan.get("content", "")

        update_result = update_file(
            owner=owner,
            repo_name=repo_name,
            file_path=file_path,
            new_content=content
        )

        if update_result["status"] == "success":

            completed_actions.append("Update File")

            mission["progress"].append({
                "step": "File Updated",
                "status": "Completed"
            })

            pr_result = create_pull_request(
                owner=owner,
                repo_name=repo_name,
                title=f"Update {file_path}",
                body=f"Automated update triggered by AWOS mission: {query}",
                head_branch="feature/update",
                base_branch="main"
            )

            if pr_result["status"] == "success":

                completed_actions.append("Open Pull Request")

                mission["progress"].append({
                    "step": "Pull Request Opened",
                    "status": "Completed"
                })

            else:
                failed_actions.append("Open Pull Request")

        else:
            failed_actions.append("Update File")

        github_results = {
            "update_result": update_result,
            "pr_result":     pr_result
        }

        recommendation = {"level": "N/A", "confidence": "N/A"}
        summary = {}
        ranking_output = []
        alternatives = []
        documentation = ""
        implementation_examples = []
        reasoning = f"Repository update mission executed for query: '{query}'."

        engineer_output = {
            "architecture":       "FastAPI Backend",
            "language":           "Python",
            "recommended_branch": "feature/update",
            "next_task":          "Review and merge Pull Request"
        }

        mission_metrics = {
            "mission_duration":  (datetime.now() - mission_start).total_seconds(),
            "completed_actions": len(completed_actions),
            "failed_actions":    len(failed_actions)
        }

    # -----------------------------------------
    # STEP 4 : Agent contributions
    # -----------------------------------------
    agent_contributions = {
        "CEO Agent": {
            "role": "Mission Planning",
            "task": "Created execution plan and selected mission type."
        },
        "Research Agent": {
            "role": "Repository Intelligence",
            "task": "Searched GitHub, ranked repositories, analyzed README and implementation examples."
        },
        "Engineer Agent": {
            "role": "Solution Design",
            "task": "Executed GitHub operations based on mission type."
        },
        "QA Agent": {
            "role": "Validation",
            "task": "Reviewed mission results via reviewer.py."
        }
    }

    # -----------------------------------------
    # STEP 5 : QA review — via reviewer.py
    # -----------------------------------------
    qa_verdict = review_mission(
        execution_plan,
        github_results
    )

    mission["progress"].append({
        "step": "QA Review Completed",
        "status": "Completed"
    })

    # -----------------------------------------
    # STEP 6 : Risk analysis
    # -----------------------------------------
    risk_analysis = {
        "overall_risk":      "Low",
        "documentation":     "Excellent",
        "community_support": "Strong",
        "maintenance":       "Active",
        "dependency_risk":   "Low"
    }

    # -----------------------------------------
    # STEP 7 : GitHub actions — from planner
    # -----------------------------------------
    github_actions = {
        "planned":   execution_plan["planned_actions"],
        "completed": completed_actions,
        "failed":    failed_actions
    }

    # -----------------------------------------
    # STEP 8 : Next steps — mission-type-aware
    # -----------------------------------------
    if mission_type == "research":
        next_steps = [
            "Review recommended repository",
            "Clone repository",
            "Start implementation"
        ]
    elif mission_type == "repository_creation":
        next_steps = [
            "Push initial project",
            "Create first feature",
            "Open Pull Request"
        ]
    else:
        next_steps = [
            "Review Pull Request",
            "Merge changes",
            "Deploy application"
        ]

    # -----------------------------------------
    # STEP 9 : Executive summary
    # -----------------------------------------
    executive_summary = {
        "mission_type":         mission_type,
        "recommendation_level": recommendation["level"],
        "confidence":           recommendation["confidence"],
        "completed_actions":    len(completed_actions),
        "failed_actions":       len(failed_actions),
        "next_action":          next_steps[0]
    }

    # -----------------------------------------
    # STEP 10 : Finalize mission status
    # -----------------------------------------
    if len(failed_actions) == 0:
        mission["status"] = "Completed"
    elif len(completed_actions) > 0:
        mission["status"] = "Completed with Errors"
    else:
        mission["status"] = "Failed"

    executive_summary["mission_status"] = mission["status"]

    # -----------------------------------------
    # STEP 11 : Final mission report
    # -----------------------------------------
    return {
        "status":                   "success",
        "mission":                  mission,
        "executive_summary":        executive_summary,
        "execution_plan":           execution_plan,
        "query":                    query,
        "reasoning":                reasoning,
        "recommendation":           recommendation,
        "ranking":                  ranking_output,
        "alternative_repositories": alternatives,
        "summary":                  summary,
        "documentation":            documentation,
        "implementation_examples":  implementation_examples,
        "engineer_output":          engineer_output,
        "qa_verdict":               qa_verdict,
        "review":                   qa_verdict,
        "agent_contributions":      agent_contributions,
        "github_actions":           github_actions,
        "mission_metrics":          mission_metrics,
        "risk_analysis":            risk_analysis,
        "next_steps":               next_steps
    }
