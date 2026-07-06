from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from config import (
    SLACK_BOT_TOKEN,
    SLACK_APP_TOKEN,
)

app = App(token=SLACK_BOT_TOKEN)


@app.event("app_mention")
def handle_mention(event, say):
    user = event["user"]
    say(f"👋 Hello <@{user}>! AWOS Bot is running successfully.")


if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()