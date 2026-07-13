from utils import current_time


def activity_block():

    return [

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "🕒 AWOS Activity Feed"
            }
        },

        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"📡 Live Activity Feed | ⏰ {current_time()}"
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
                "🟢 *Mission Created*\n"
                "`Create Login API`\n"
                f"⏰ {current_time()}"
            }
        },

        {
            "type": "divider"
        },

        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text":
                "▶ *Mission Executed*\n"
                "`Create Dashboard UI`\n"
                f"⏰ {current_time()}"
            }
        },

        {
            "type": "divider"
        },

        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text":
                "📊 *Analytics Dashboard Viewed*\n"
                f"⏰ {current_time()}"
            }
        },

        {
            "type": "divider"
        },

        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text":
                "👑 *CEO Dashboard Opened*\n"
                f"⏰ {current_time()}"
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
                    "🚀 Powered by AWOS Genesis • Activity Feed"
                }
            ]
        }

    ]