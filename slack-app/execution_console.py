from utils import current_time


def execution_console_block(mission):

    return [

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "🧠 AWOS Execution Console"
            }
        },

        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"⏰ {current_time()}   |   🚀 Mission Accepted"
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
                    "text": f"*🟢 Status*\n{mission['status']}"
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
                "*🤖 AI Workflow*\n\n"
                "⏳ Waiting for backend execution...\n"
                "The AI engine will stream progress here once execution starts."
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
                    "🧠 Powered by AWOS Genesis • Execution Console"
                }
            ]
        }

    ]