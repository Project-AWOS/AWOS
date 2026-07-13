from utils import current_time


def search_block(query, missions):

    blocks = [

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "🔍 AWOS Mission Search"
            }
        },

        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"Query: *{query}*   |   ⏰ {current_time()}"
                }
            ]
        },

        {
            "type": "divider"
        }

    ]

    if not missions:

        blocks.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "❌ No matching missions found."
                }
            }
        )

        return blocks

    for mission in missions:

        status = mission["status"]

        if status == "Created":
            icon = "🟢"
        elif status == "Running":
            icon = "🟡"
        elif status == "Completed":
            icon = "✅"
        elif status == "Failed":
            icon = "❌"
        else:
            icon = "⚪"

        blocks.extend([

            {
                "type": "section",
                "fields": [

                    {
                        "type": "mrkdwn",
                        "text": f"*📌 Mission*\n{mission['title']}"
                    },

                    {
                        "type": "mrkdwn",
                        "text": f"*🆔 ID*\n{mission['mission_id']}"
                    },

                    {
                        "type": "mrkdwn",
                        "text": f"*🔥 Priority*\n{mission['priority']}"
                    },

                    {
                        "type": "mrkdwn",
                        "text": f"*{icon} Status*\n{status}"
                    }

                ]
            },

            {
                "type": "divider"
            }

        ])

    return blocks