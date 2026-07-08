import requests
from config import FASTAPI_URL


def register_listeners(app):

    @app.event("app_mention")
    def handle_mention(event, say):
        user = event["user"]
        say(f"👋 Hello <@{user}>! AWOS Bot is running successfully.")

    @app.command("/awos")
    def handle_awos_command(ack, respond, command):
        ack()

        text = command["text"]

        payload = {
            "title": text,
            "objective": text,
            "priority": "Medium"
        }

        try:
            response = requests.post(
                f"{FASTAPI_URL}/missions/",
                json=payload,
                timeout=30
            )

            data = response.json()

            respond(
                f"""✅ Mission Created!

Mission ID: {data['mission_id']}
Title: {data['title']}
Priority: {data['priority']}
Status: {data['status']}
"""
            )

        except Exception as e:
            respond(f"❌ Failed to create mission.\n\n{e}")