"""
Friday Backend — API v1 Router

Central router that aggregates all v1 API endpoints.
"""

from fastapi import APIRouter

api_router = APIRouter()


@api_router.get("/ping")
async def ping():
    """Simple ping endpoint to verify API is working."""
    return {"message": "pong"}
