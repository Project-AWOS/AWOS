from utils import current_time


def dashboard_block(missions):
    """
    Professional AWOS Dashboard
    """

    # ===============================
    # Live Statistics
    # ===============================

    total = len(missions)

    created = sum(
        1 for mission in missions
        if mission["status"] == "Created"
    )

    running = sum(
        1 for mission in missions
        if mission["status"] == "Running"
    )

    completed = sum(
        1 for mission in missions
        if mission["status"] == "Completed"
    )

    failed = sum(
        1 for mission in missions
        if mission["status"] == "Failed"
    )

    return [

        # ===================================
        # Header
        # ===================================

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "🚀 AWOS Genesis Dashboard"
            }
        },

        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text":
                        f"🧠 Autonomous Workforce Operating System   |   ⏰ {current_time()}"
                }
            ]
        },

        {
            "type": "divider"
        },

        # ===================================
        # System Overview
        # ===================================

        {
            "type": "section",
            "fields": [

                {
                    "type": "mrkdwn",
                    "text": "*🟢 System Status*\nOnline"
                },

                {
                    "type": "mrkdwn",
                    "text": "*🤖 AI Engine*\nGemini"
                },

                {
                    "type": "mrkdwn",
                    "text": f"*📋 Total Missions*\n{total}"
                },

                {
                    "type": "mrkdwn",
                    "text": f"*⚡ Running*\n{running}"
                },

                {
                    "type": "mrkdwn",
                    "text": f"*✅ Completed*\n{completed}"
                },

                {
                    "type": "mrkdwn",
                    "text": f"*🟢 Created*\n{created}"
                },

                {
                    "type": "mrkdwn",
                    "text": f"*❌ Failed*\n{failed}"
                },

                {
                    "type": "mrkdwn",
                    "text": "*🖥 Backend*\nConnected"
                }

            ]
        },

        {
            "type": "divider"
        },

        # ===================================
        # Active Workforce
        # ===================================

        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text":
                    "*🤖 Active AI Workforce*\n\n"
                    "👑 CEO Agent        🟢 Ready\n"
                    "🔬 Research Agent   🟢 Ready\n"
                    "🧠 Reasoner         🟢 Ready\n"
                    "👨‍💻 Engineer        🟢 Ready\n"
                    "🧪 QA Agent         🟢 Ready"
            }
        },

        {
            "type": "divider"
        },

        # ===================================
        # Quick Actions
        # ===================================

        {
            "type": "actions",
            "elements": [

                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "📋 View Missions"
                    },
                    "action_id": "view_missions"
                },

                {
                    "type": "button",
                    "style": "primary",
                    "text": {
                        "type": "plain_text",
                        "text": "🚀 Create Mission"
                    },
                    "action_id": "create_new"
                }

            ]
        },

        {
            "type": "divider"
        },

        # ===================================
        # Footer
        # ===================================

        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text":
                        "🚀 Powered by AWOS Genesis • Autonomous Workforce Operating System"
                }
            ]
        }

    ]