from fastapi import FastAPI

from app.routers import mission, analytics

app = FastAPI(
    title="AWOS Core",
    description="Autonomous Workforce Operating System",
    version="Genesis v1.0"
)

app.include_router(mission.router)
app.include_router(analytics.router)


@app.get("/")
async def root():
    return {
        "system": "AWOS",
        "version": "Genesis v1.0",
        "status": "Operational",
        "brain": {
            "name": "CORTEX",
            "status": "Online"
        },
        "operations": {
            "name": "HELIX",
            "status": "Online"
        },
        "message": "Welcome to AWOS - Autonomous Workforce Operating System"
    }