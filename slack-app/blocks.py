from utils import current_time


def mission_created_block(data):
    """
    Creates a professional Slack Block Kit card
    for a newly created AWOS mission.
    """

    return [

        # =========================
        # Header
        # =========================
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "🚀 AWOS Mission Control"
            }
        },

        # =========================
        # System Status
        # =========================
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": (
                        f"🧠 *AWOS Genesis*   |   "
                        f"⏰ {current_time()}   |   "
                        f"🟢 System Online"
                    )
                }
            ]
        },

        {
            "type": "divider"
        },

        # =========================
        # Mission Information
        # =========================
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

        # =========================
        # Objective
        # =========================
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*🎯 Objective*\n{data['objective']}"
            }
        },

        {
            "type": "divider"
        },

        # =========================
        # AI Status
        # =========================
        {
            "type": "section",
            "fields": [

                {
                    "type": "mrkdwn",
                    "text": "*🤖 Assigned Agent*\nPending"
                },

                {
                    "type": "mrkdwn",
                    "text": "*🧠 AI Engine*\nGemini (Configured)"
                },

                {
                    "type": "mrkdwn",
                    "text": "*📊 Complexity*\nTo Be Analyzed"
                },

                {
                    "type": "mrkdwn",
                    "text": "*⚙ Workflow*\nReady for Execution"
                }

            ]
        },

        {
            "type": "divider"
        },

        # =========================
        # Action Buttons
        # =========================
        {
            "type": "actions",
            "elements": [

                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "▶ Execute"
                    },
                    "style": "primary",
                    "action_id": "execute_mission",
                    "value": data["mission_id"]
                },

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
            "type": "divider"
        },

        # =========================
        # Footer
        # =========================
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": (
                        "🚀 *Powered by AWOS* • "
                        "Autonomous Workforce Operating System"
                    )
                }
            ]
        }

    ]