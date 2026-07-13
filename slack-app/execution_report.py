from utils import current_time


def execution_report_block(mission, result):

    return [

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "✅ AWOS Mission Execution Report"
            }
        },

        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"⏰ {current_time()} • Mission Completed"
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
                    "text": "*🏁 Status*\nCompleted"
                },

                {
                    "type": "mrkdwn",
                    "text": "*🤖 Workflow*\n5/5 Agents Finished"
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
                "👑 CEO Agent          ✅ Completed\n"
                "🔬 Research Agent     ✅ Completed\n"
                "🧠 Reasoner           ✅ Completed\n"
                "👨‍💻 Engineer          ✅ Completed\n"
                "🧪 QA Agent           ✅ Completed"
            }
        },

        {
            "type": "divider"
        },

        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*📄 Execution Result*\n```{result}```"
            }
        }

    ]