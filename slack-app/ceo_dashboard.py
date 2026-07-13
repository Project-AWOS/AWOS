from utils import current_time


def ceo_dashboard_block(data):

    total_agents = 5

    # =====================================================
    # Dynamic Values
    # =====================================================

    if data["failed"] == 0:
        recommendation = "✅ No failed missions detected."
    else:
        recommendation = "⚠ Review failed missions immediately."

    if data["running"] == 0:
        workload = "🟢 Low"
    elif data["running"] <= 3:
        workload = "🟡 Moderate"
    else:
        workload = "🔴 High"

    if data["success_rate"] >= 90:
        health = "🟢 Excellent"
    elif data["success_rate"] >= 70:
        health = "🟡 Good"
    else:
        health = "🔴 Needs Attention"

    return [

        # =====================================================
        # Header
        # =====================================================

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "👑 AWOS CEO Command Center"
            }
        },

        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"🧠 Executive Dashboard | ⏰ {current_time()}"
                }
            ]
        },

        {
            "type": "divider"
        },

        # =====================================================
        # Executive Summary
        # =====================================================

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "👑 Executive Summary"
            }
        },

        {
            "type": "section",
            "fields": [

                {
                    "type": "mrkdwn",
                    "text": f"*💚 Overall Health*\n{health}"
                },

                {
                    "type": "mrkdwn",
                    "text": "*🎯 Priority Focus*\nMission Monitoring"
                },

                {
                    "type": "mrkdwn",
                    "text": f"*⚡ Workforce Load*\n{workload}"
                },

                {
                    "type": "mrkdwn",
                    "text": "*📈 Business Status*\nOperational"
                }

            ]
        },

        {
            "type": "divider"
        },

        # =====================================================
        # Infrastructure
        # =====================================================

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "⚙ Infrastructure"
            }
        },

        {
            "type": "section",
            "fields": [

                {
                    "type": "mrkdwn",
                    "text": "*🟢 Backend*\nHealthy"
                },

                {
                    "type": "mrkdwn",
                    "text": "*🟢 Slack*\nConnected"
                },

                {
                    "type": "mrkdwn",
                    "text": "*🟢 LangGraph*\nRunning"
                },

                {
                    "type": "mrkdwn",
                    "text": "*🟡 Gemini*\nPending Configuration"
                }

            ]
        },

        {
            "type": "divider"
        },

        # =====================================================
        # Executive Overview
        # =====================================================

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "📊 Executive Overview"
            }
        },

        {
            "type": "section",
            "fields": [

                {
                    "type": "mrkdwn",
                    "text": f"*📋 Total Missions*\n{data['total_missions']}"
                },

                {
                    "type": "mrkdwn",
                    "text": f"*🟢 Created*\n{data['created']}"
                },

                {
                    "type": "mrkdwn",
                    "text": f"*⚡ Running*\n{data['running']}"
                },

                {
                    "type": "mrkdwn",
                    "text": f"*✅ Completed*\n{data['completed']}"
                },

                {
                    "type": "mrkdwn",
                    "text": f"*❌ Failed*\n{data['failed']}"
                },

                {
                    "type": "mrkdwn",
                    "text": f"*📈 Success Rate*\n{data['success_rate']}%"
                }

            ]
        },

        {
            "type": "divider"
        },

        # =====================================================
        # Workforce Status
        # =====================================================

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "🤖 Workforce Status"
            }
        },

        {
            "type": "section",
            "fields": [

                {
                    "type": "mrkdwn",
                    "text": "👑 CEO Agent\n🟢 Monitoring"
                },

                {
                    "type": "mrkdwn",
                    "text": "🔬 Research Agent\n🟢 Available"
                },

                {
                    "type": "mrkdwn",
                    "text": "🧠 Reasoner\n🟢 Idle"
                },

                {
                    "type": "mrkdwn",
                    "text": "👨‍💻 Engineer\n🟢 Available"
                },

                {
                    "type": "mrkdwn",
                    "text": "🧪 QA Agent\n🟢 Available"
                }

            ]
        },

        {
            "type": "divider"
        },

        # =====================================================
        # Operations
        # =====================================================

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "⚙ Operations"
            }
        },

        {
            "type": "section",
            "fields": [

                {
                    "type": "mrkdwn",
                    "text": f"*👥 Active Agents*\n{total_agents}"
                },

                {
                    "type": "mrkdwn",
                    "text": f"*💚 System Health*\n{health}"
                },

                {
                    "type": "mrkdwn",
                    "text": f"*📦 Workload*\n{workload}"
                },

                {
                    "type": "mrkdwn",
                    "text": "*🧠 AI Engine*\nGemini"
                }

            ]
        },

        {
            "type": "divider"
        },

        # =====================================================
        # Strategic Insights
        # =====================================================

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "🧠 Strategic Insights"
            }
        },

        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text":
                f"{recommendation}\n"
                "📈 Mission pipeline healthy.\n"
                "🚀 Workforce operating efficiently.\n"
                "🧠 CEO recommends accepting new missions."
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
                    f"👑 AWOS CEO Intelligence Engine • Last Updated {current_time()}"
                }
            ]
        }

    ]