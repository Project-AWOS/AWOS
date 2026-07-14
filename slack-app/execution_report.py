from utils import current_time


def execution_report_block(mission, result):

    plan = result["execution_plan"]

    steps = ""

    for step in plan["steps"]:
        steps += (
            f"• *Step {step['order']}*\n"
            f"🤖 {step['agent']} Agent\n"
            f"➡ {step['action']}\n\n"
        )

    tools = ""

    for tool in plan["tools"]:
        tools += f"• {tool}\n"

    return [

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "📄 AWOS Execution Report"
            }
        },

        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"⏰ {current_time()} • ✅ Execution Completed"
                }
            ]
        },

        {
            "type": "divider"
        },

        {
            "type": "section",
            "fields": [

                {
                    "type": "mrkdwn",
                    "text": f"*📌 Mission*\n{mission['title']}"
                },

                {
                    "type": "mrkdwn",
                    "text": f"*🆔 Mission ID*\n{mission['mission_id']}"
                },

                {
                    "type": "mrkdwn",
                    "text": f"*🔥 Priority*\n{mission['priority']}"
                },

                {
                    "type": "mrkdwn",
                    "text": "*🏁 Status*\nCompleted"
                }

            ]
        },

        {
            "type": "divider"
        },

        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text":
                f"*📝 AI Summary*\n\n"
                f"{plan['summary']}"
            }
        },

        {
            "type": "divider"
        },

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "🤖 Execution Workflow"
            }
        },

        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": steps
            }
        },

        {
            "type": "divider"
        },

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "🛠 AI Tools Used"
            }
        },

        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": tools
            }
        },

        {
            "type": "divider"
        },

        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text":
                    "🚀 Powered by AWOS Genesis • Demo Mode"
                }
            ]
        }

    ]