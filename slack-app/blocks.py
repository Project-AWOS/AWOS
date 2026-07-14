from utils import current_time


def mission_created_block(data):

    return [

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "🚀 AWOS Mission Created"
            }
        },

        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"🧠 AWOS Genesis | ⏰ {current_time()} | 🟢 System Online"
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
                    "text": f"*📌 Mission*\n{data['title']}"
                },

                {
                    "type": "mrkdwn",
                    "text": f"*🆔 Mission ID*\n{data['mission_id']}"
                },

                {
                    "type": "mrkdwn",
                    "text": f"*🔥 Priority*\n{data['priority']}"
                },

                {
                    "type": "mrkdwn",
                    "text": f"*🟢 Status*\n{data['status']}"
                }

            ]
        },

        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text":
                "✅ Mission created successfully.\n\n"
                "➡ Next step:\n"
                "Run `/awos missions` and execute the mission from the Mission Center."
            }
        },

        {
            "type": "divider"
        },

        {
            "type": "actions",
            "elements": [

                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "📄 Details"
                    },
                    "action_id": "view_details",
                    "value": data["mission_id"]
                },

                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "🗑 Delete"
                    },
                    "style": "danger",
                    "action_id": "delete_mission",
                    "value": data["mission_id"]
                }

            ]
        },

        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "🚀 Powered by AWOS Genesis"
                }
            ]
        }

    ]