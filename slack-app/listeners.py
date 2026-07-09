from commands import handle_command

from awos_client import (
    execute_mission,
    get_mission,
    delete_mission,
)

from execution_console import execution_console_block


def register_listeners(app):

    # =====================================================
    # App Mention
    # =====================================================

    @app.event("app_mention")
    def handle_mention(event, say):
        user = event["user"]

        say(
            f"👋 Hello <@{user}>!\n\n"
            f"🚀 AWOS Mission Control is Online."
        )

    # =====================================================
    # Slash Command
    # =====================================================

    @app.command("/awos")
    def handle_awos_command(ack, respond, command):
        ack()

        handle_command(
            command["text"],
            respond
        )

    # =====================================================
    # Execute Mission
    # =====================================================

    @app.action("execute_mission")
    def execute_button(ack, body, respond):
        ack()

        mission_id = body["actions"][0]["value"]

        try:

            # Fetch mission first
            mission = get_mission(mission_id)

            # Show beautiful execution console
            respond(
                text="🧠 AWOS Execution Console",
                blocks=execution_console_block(mission)
            )

            # Execute mission
            execute_mission(mission_id)

        except Exception as e:

            respond(
                text=
                "❌ Unable to execute mission.\n\n"
                f"{str(e)}"
            )

    # =====================================================
    # View Details
    # =====================================================

    @app.action("view_details")
    def details_button(ack, body, respond):
        ack()

        mission_id = body["actions"][0]["value"]

        try:

            mission = get_mission(mission_id)

            respond(
                text="📄 Mission Details",
                blocks=[
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "📄 AWOS Mission Details"
                        }
                    },

                    {
                        "type": "divider"
                    },

                    {
                        "type": "section",
                        "fields": [

                            {
                                "type": "mrkdwn",
                                "text":
                                f"*📌 Mission*\n{mission['title']}"
                            },

                            {
                                "type": "mrkdwn",
                                "text":
                                f"*🆔 Mission ID*\n{mission['mission_id']}"
                            },

                            {
                                "type": "mrkdwn",
                                "text":
                                f"*🔥 Priority*\n{mission['priority']}"
                            },

                            {
                                "type": "mrkdwn",
                                "text":
                                f"*🟢 Status*\n{mission['status']}"
                            }

                        ]
                    },

                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text":
                            f"*🎯 Objective*\n{mission['objective']}"
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
                                "🚀 Powered by AWOS Genesis"
                            }
                        ]
                    }
                ]
            )

        except Exception as e:

            respond(
                text=
                "❌ Unable to fetch mission details.\n\n"
                f"{str(e)}"
            )

    # =====================================================
    # Delete Mission
    # =====================================================

    @app.action("delete_mission")
    def delete_button(ack, body, respond):
        ack()

        mission_id = body["actions"][0]["value"]

        try:

            delete_mission(mission_id)

            respond(
                text=
                "🗑 Mission deleted successfully."
            )

        except Exception as e:

            respond(
                text=
                "❌ Unable to delete mission.\n\n"
                f"{str(e)}"
            )