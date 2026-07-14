import threading
import time
import webbrowser

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from config import SLACK_BOT_TOKEN, SLACK_APP_TOKEN
from listeners import register_listeners

app = App(token=SLACK_BOT_TOKEN)

register_listeners(app)


def open_slack():
    time.sleep(2)
    webbrowser.open(
        "https://app.slack.com/client/T0BF6GVF2TB/C0BF2K5S7E"
    )


if __name__ == "__main__":

    print("=" * 50)
    print("🚀 AWOS Mission Control Started")
    print("=" * 50)

    threading.Thread(target=open_slack, daemon=True).start()

    SocketModeHandler(
        app,
        SLACK_APP_TOKEN
    ).start()