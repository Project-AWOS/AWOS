from github_mcp.workflow import execute_github_research_mission


def main():
    try:

        query = "FastAPI authentication"

        result = execute_github_research_mission(query)

        print("=" * 80)
        print("AWOS GitHub Research Workflow Test")
        print("=" * 80)

        print(f"Status      : {result.get('status')}")

        if result.get("status") != "success":
            print(result.get("message"))
            return

        print(f"Mission ID  : {result['mission']['mission_id']}")
        print(f"Mission     : {result['mission']['mission_name']}")
        print(f"Query       : {result['query']}")
        print()

        print("=" * 80)
        print("Selected Repository")
        print("=" * 80)

        if result["ranking"]:

            top_repo = result["ranking"][0]

            print(f"Repository : {top_repo['repository']}")
            print(f"Stars      : {top_repo['stars']}")
            print(f"Score      : {top_repo['score']}")

        else:

            print("No repository ranking available.")

        print()

        print("=" * 80)
        print("Reasoning")
        print("=" * 80)

        print(result["reasoning"])
        print()

        print("=" * 80)
        print("Recommendation")
        print("=" * 80)

        recommendation = result["recommendation"]

        print(f"Level       : {recommendation['level']}")
        print(f"Confidence  : {recommendation['confidence']}")
        print(f"Reason      : {recommendation['reason']}")
        print(f"Use Case    : {recommendation['use_case']}")
        print()

        print("=" * 80)
        print("Repository Summary")
        print("=" * 80)

        summary = result["summary"]

        if summary:

            print(f"Description : {summary['description']}")
            print(f"Stars       : {summary['stars']}")
            print(f"Forks       : {summary['forks']}")
            print(f"Language    : {summary['language']}")
            print(f"Open Issues : {summary['open_issues']}")
            print(f"Branch      : {summary['default_branch']}")
            print(f"URL         : {summary['url']}")

        else:

            print("No repository summary available.")

        print()

        print("=" * 80)
        print("Executive Summary")
        print("=" * 80)

        executive = result["executive_summary"]

        for key, value in executive.items():
            print(f"{key:22}: {value}")

        print()

        print("=" * 80)
        print("QA Verdict")
        print("=" * 80)

        print(result["qa_verdict"])
        print()

        print("=" * 80)
        print("Mission Metrics")
        print("=" * 80)

        metrics = result["mission_metrics"]

        print(
            f"Repositories Analysed : {metrics.get('repositories_analyzed', 'N/A')}")
        print(
            f"Examples Found        : {metrics.get('implementation_examples', 'N/A')}")
        print(f"Confidence            : {metrics.get('confidence', 'N/A')}")
        print(
            f"Mission Duration      : {metrics.get('mission_duration', 'N/A')}")

        print()

        print("=" * 80)
        print("Next Steps")
        print("=" * 80)

        for step in result["next_steps"]:
            print(f"• {step}")

        print()

        print("=" * 80)
        print("Workflow Test Completed Successfully")
        print("=" * 80)

    except Exception as e:

        print("❌ Workflow Test Failed")
        print(e)


if __name__ == "__main__":
    main()
