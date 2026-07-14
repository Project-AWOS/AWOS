def missions_block(missions):
    """
    Builds 🚀 AWOS Mission Control.
    """

    blocks = [

        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "📋 AWOS Mission Center"
            }
        },

        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"🚀 Total Missions: *{len(missions)}*"
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
                    "text": "No missions found."
                }
            }
        )

        return blocks

    for mission in missions:

        status = mission.get("status", "Unknown")

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

        blocks.extend(

            [

                {
                    "type": "section",
                    "fields": [

                        {
                            "type": "mrkdwn",
                            "text": f"*📌 Mission*\n{mission['title']}"
                        },

                        {
                            "type": "mrkdwn",
                            "text": f"*🎯 Objective*\n{mission['objective']}"
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
                    "type": "actions",
                    "elements": [

                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "📄 Details"
                            },
                            "value": mission["mission_id"],
                            "action_id": "view_details"
                        },

                        {
                            "type": "button",
                            "style": "primary",
                            "text": {
                                "type": "plain_text",
                                "text": "🌐 Open GitHub"
                            },
                            "url": "https://github.com/search?q=cybersecurity+projects&type=repositories"
                        },

                        {
                            "type": "button",
                            "style": "danger",
                            "text": {
                                "type": "plain_text",
                                "text": "🗑 Delete"
                            },
                            "value": mission["mission_id"],
                            "action_id": "delete_mission"
                        }

                    ]
                },

                {
                    "type": "divider"
                }

            ]

        )

    return blocks