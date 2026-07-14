from awos_client import (
    create_mission,
    get_missions,
    get_analytics,
)

from blocks import mission_created_block
from dashboard import dashboard_block
from missions import missions_block
from analytics import analytics_block
from ceo_dashboard import ceo_dashboard_block
from search import search_block
from activity import activity_block
from mission_queue import queue_block


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
            text=(
                "❌ Please enter a command.\n\n"
                "Examples:\n"
                "/awos dashboard\n"
                "/awos missions\n"
                "/awos analytics\n"
                "/awos ceo\n"
                "/awos activity\n"
                "/awos queue\n"
                "/awos search login\n"
                "/awos Create Login API"
            )
        )
        return

    # ==========================================
    # Mission Search
    # ==========================================

    if text.lower().startswith("search "):

        query = text[7:].strip()

        missions = get_missions()

        results = []

        for mission in missions:

            searchable = (
                mission["title"] + " " +
                mission["objective"] + " " +
                mission["status"] + " " +
                mission["priority"] + " " +
                mission["mission_id"]
            ).lower()

            if query.lower() in searchable:
                results.append(mission)

        respond(
            text=f"🔍 Search Results for '{query}'",
            blocks=search_block(query, results)
        )

        return

    # ==========================================
    # Mission Queue
    # ==========================================

    if text.lower() == "queue":

        missions = get_missions()

        respond(
            text="📌 AWOS Mission Queue",
            blocks=queue_block(missions)
        )

        return

    # ==========================================
    # Activity Feed
    # ==========================================

    if text.lower() == "activity":

        respond(
            text="🕒 AWOS Activity Feed",
            blocks=activity_block()
        )

        return

    # ==========================================
    # CEO Dashboard
    # ==========================================

    if text.lower() == "ceo":

        analytics = get_analytics()

        respond(
            text="👑 AWOS CEO Command Center",
            blocks=ceo_dashboard_block(analytics)
        )

        return

    # ==========================================
    # Analytics
    # ==========================================

    if text.lower() == "analytics":

        analytics = get_analytics()

        respond(
            text="📊 AWOS Analytics",
            blocks=analytics_block(analytics)
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