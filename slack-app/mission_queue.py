from utils import current_time


def queue_block(missions):

    priority_order = {
        "High": 0,
        "Medium": 1,
        "Low": 2,
    }

    missions = sorted(
        missions,
        key=lambda m: priority_order.get(
            m.get("priority", "Low"),
            3
        )
    )

    blocks = [

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "📌 AWOS Mission Queue"
            }
        },

        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"📋 Mission Execution Queue | ⏰ {current_time()}"
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
                    "text": "📭 No missions available in the queue."
                }
            }
        )

        return blocks

    high = 0
    medium = 0
    low = 0

    for index, mission in enumerate(missions, start=1):

        priority = mission["priority"]

        if priority == "High":
            icon = "🔥"
            high += 1
        elif priority == "Medium":
            icon = "🟡"
            medium += 1
        else:
            icon = "🟢"
            low += 1

        status = mission["status"]

        if status == "Created":
            status_icon = "🟢"
        elif status == "Running":
            status_icon = "🟡"
        elif status == "Completed":
            status_icon = "✅"
        elif status == "Failed":
            status_icon = "❌"
        else:
            status_icon = "⚪"

        blocks.extend(

            [

                {
                    "type": "section",
                    "fields": [

                        {
                            "type": "mrkdwn",
                            "text":
                            f"*{index}. {mission['title']}*"
                        },

                        {
                            "type": "mrkdwn",
                            "text":
                            f"{icon} *Priority*\n{priority}"
                        },

                        {
                            "type": "mrkdwn",
                            "text":
                            f"{status_icon} *Status*\n{status}"
                        },

                        {
                            "type": "mrkdwn",
                            "text":
                            f"🆔 *Mission ID*\n{mission['mission_id']}"
                        }

                    ]
                },

                {
                    "type": "divider"
                }

            ]

        )

    blocks.extend(

        [

            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "📊 Queue Summary"
                }
            },

            {
                "type": "section",
                "fields": [

                    {
                        "type": "mrkdwn",
                        "text":
                        f"*📋 Total Missions*\n{len(missions)}"
                    },

                    {
                        "type": "mrkdwn",
                        "text":
                        f"*🔥 High Priority*\n{high}"
                    },

                    {
                        "type": "mrkdwn",
                        "text":
                        f"*🟡 Medium Priority*\n{medium}"
                    },

                    {
                        "type": "mrkdwn",
                        "text":
                        f"*🟢 Low Priority*\n{low}"
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
                        "📌 Powered by AWOS Genesis • Mission Queue"
                    }
                ]
            }

        ]

    )

    return blocks