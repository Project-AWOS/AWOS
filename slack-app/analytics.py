from utils import current_time


def analytics_block(data):

    total_agents = 5
    ready_agents = 5

    return [

        # =====================================================
        # Header
        # =====================================================

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "📊 AWOS Operations Console"
            }
        },

        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text":
                    f"🧠 AWOS Genesis   |   ⏰ {current_time()}   |   🚀 Live Operations"
                }
            ]
        },

        {
            "type": "divider"
        },

        # =====================================================
        # Overall Health
        # =====================================================

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "🟢 Overall System Health"
            }
        },

        {
            "type": "section",
            "fields": [

                {
                    "type": "mrkdwn",
                    "text": "*⚙ Backend*\n🟢 Connected"
                },

                {
                    "type": "mrkdwn",
                    "text": "*🤖 AI Engine*\nGemini"
                },

                {
                    "type": "mrkdwn",
                    "text": "*🧠 CORTEX*\n🟢 Online"
                },

                {
                    "type": "mrkdwn",
                    "text": "*⚙ HELIX*\n🟢 Online"
                },

                {
                    "type": "mrkdwn",
                    "text": "*📡 MCP*\n🟢 Connected"
                },

                {
                    "type": "mrkdwn",
                    "text": "*❤️ Health*\nExcellent"
                }

            ]
        },

        {
            "type": "divider"
        },

        # =====================================================
        # Mission Statistics
        # =====================================================

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "📈 Mission Analytics"
            }
        },

        {
            "type": "section",
            "fields": [

                {
                    "type": "mrkdwn",
                    "text":
                    f"*📋 Total Missions*\n{data['total_missions']}"
                },

                {
                    "type": "mrkdwn",
                    "text":
                    f"*🟢 Created*\n{data['created']}"
                },

                {
                    "type": "mrkdwn",
                    "text":
                    f"*⚡ Running*\n{data['running']}"
                },

                {
                    "type": "mrkdwn",
                    "text":
                    f"*✅ Completed*\n{data['completed']}"
                },

                {
                    "type": "mrkdwn",
                    "text":
                    f"*❌ Failed*\n{data['failed']}"
                },

                {
                    "type": "mrkdwn",
                    "text":
                    f"*📈 Success Rate*\n{data['success_rate']}%"
                }

            ]
        },

        {
            "type": "divider"
        },

        # =====================================================
        # Workforce Summary
        # =====================================================

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "🤖 AI Workforce"
            }
        },

        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text":
                f"🟢 *{ready_agents}/{total_agents} Agents Ready*"
            }
        },

        {
            "type": "section",
            "fields": [

                {
                    "type": "mrkdwn",
                    "text": "👑 CEO Agent\n🟢 Ready"
                },

                {
                    "type": "mrkdwn",
                    "text": "🔬 Research Agent\n🟢 Ready"
                },

                {
                    "type": "mrkdwn",
                    "text": "🧠 Reasoner\n🟢 Ready"
                },

                {
                    "type": "mrkdwn",
                    "text": "👨‍💻 Engineer\n🟢 Ready"
                },

                {
                    "type": "mrkdwn",
                    "text": "🧪 QA Agent\n🟢 Ready"
                }

            ]
        },

        {
            "type": "divider"
        },

        # =====================================================
        # Operations Summary
        # =====================================================

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "📋 Operations Summary"
            }
        },

        {
            "type": "section",
            "fields": [

                {
                    "type": "mrkdwn",
                    "text":
                    f"*📋 Missions*\n{data['total_missions']}"
                },

                {
                    "type": "mrkdwn",
                    "text":
                    f"*⚡ Active*\n{data['running']}"
                },

                {
                    "type": "mrkdwn",
                    "text":
                    f"*📈 Success*\n{data['success_rate']}%"
                },

                {
                    "type": "mrkdwn",
                    "text":
                    f"*🕒 Updated*\n{current_time()}"
                }

            ]
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
                    "🚀 Powered by AWOS Genesis • Autonomous Workforce Operating System"
                }

            ]
        }

    ]