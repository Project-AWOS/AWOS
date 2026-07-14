from utils import current_time


def execution_console_block(mission):

    return [

        # =====================================================
        # Header
        # =====================================================

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "🚀 AWOS Live Mission Timeline"
            }
        },

        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text":
                    f"🧠 AWOS Genesis   |   ⏰ {current_time()}   |   🟡 Executing"
                }
            ]
        },

        {
            "type": "divider"
        },

        # =====================================================
        # Mission Information
        # =====================================================

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
                    "text": "*⚡ Status*\nExecuting"
                }

            ]
        },

        {
            "type": "divider"
        },

        # =====================================================
        # Timeline
        # =====================================================

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "🤖 AI Agent Timeline"
            }
        },

        {
            "type": "section",
            "fields": [

                {
                    "type": "mrkdwn",
                    "text":
                    "👑 *CEO Agent*\n"
                    "🟢 Mission Accepted"
                },

                {
                    "type": "mrkdwn",
                    "text":
                    "🔬 *Research Agent*\n"
                    "🟡 Analyzing Requirements..."
                },

                {
                    "type": "mrkdwn",
                    "text":
                    "🧠 *Reasoner*\n"
                    "⚪ Waiting"
                },

                {
                    "type": "mrkdwn",
                    "text":
                    "👨‍💻 *Engineer*\n"
                    "⚪ Waiting"
                },

                {
                    "type": "mrkdwn",
                    "text":
                    "🧪 *QA Agent*\n"
                    "⚪ Waiting"
                }

            ]
        },

        {
            "type": "divider"
        },

        # =====================================================
        # Progress
        # =====================================================

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "📈 Execution Progress"
            }
        },

        {
            "type": "section",
            "fields": [

                {
                    "type": "mrkdwn",
                    "text":
                    "*Progress*\n"
                    "██░░░░░░░░ 20%"
                },

                {
                    "type": "mrkdwn",
                    "text":
                    "*Current Stage*\n"
                    "Research Agent"
                },

                {
                    "type": "mrkdwn",
                    "text":
                    "*Estimated Time*\n"
                    "~2 min"
                },

                {
                    "type": "mrkdwn",
                    "text":
                    "*AI Engine*\n"
                    "Gemini"
                }

            ]
        },

        {
            "type": "divider"
        },

        # =====================================================
        # Activity Feed
        # =====================================================

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "📜 Live Activity"
            }
        },

        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text":
                "✅ CEO Agent accepted mission\n"
                "🟡 Research Agent gathering context\n"
                "⚪ Waiting for reasoning phase..."
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
                    f"🚀 Powered by AWOS Genesis • Last Updated {current_time()}"
                }
            ]
        }

    ]