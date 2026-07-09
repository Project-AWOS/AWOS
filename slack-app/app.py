from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from config import SLACK_BOT_TOKEN, SLACK_APP_TOKEN
from listeners import register_listeners

app = App(token=SLACK_BOT_TOKEN)

register_listeners(app)

if __name__ == "__main__":
    print("=" * 50)
    print("🚀 AWOS Mission Control Started")
    print("=" * 50)

    SocketModeHandler(
        app,
        SLACK_APP_TOKEN
    ).start()