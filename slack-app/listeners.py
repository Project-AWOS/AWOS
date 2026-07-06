def register_listeners(app):

    @app.event("app_mention")
    def handle_mention(event, say):
        user = event["user"]
        say(f"👋 Hello <@{user}>! AWOS Bot is running successfully.")

    @app.command("/awos")
    def handle_awos_command(ack, respond, command):
        ack()

        text = command["text"]

        respond(
            f"🚀 AWOS received your request:\n\n"
            f"> {text}"
        )