from awos_client import create_mission, get_missions
from blocks import mission_created_block
from dashboard import dashboard_block
from missions import missions_block


def handle_command(text, respond):
    """
    Routes incoming Slack commands.
    """

    text = text.strip()

    # ==========================================
    # Empty Command
    # ==========================================

    if not text:
        respond(
            text="❌ Please enter a mission.\nExample:\n/awos Create Login API"
        )
        return

    # ==========================================
    # Mission Center
    # ==========================================

    if text.lower() == "missions":

        missions = get_missions()

        respond(
            text="📋 AWOS Mission Center",
            blocks=missions_block(missions)
        )

        return

    # ==========================================
    # Dashboard
    # ==========================================

    if text.lower() == "dashboard":

        missions = get_missions()

        respond(
            text="🚀 AWOS Dashboard",
            blocks=dashboard_block(missions)
        )

        return

    # ==========================================
    # Create Mission
    # ==========================================

    try:

        mission = create_mission(text)

        respond(
            text="🚀 AWOS Mission Created",
            blocks=mission_created_block(mission)
        )

    except Exception as e:

        respond(
            text=f"❌ Failed to create mission.\n\n{str(e)}"
        )