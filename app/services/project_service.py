from typing import Dict
import uuid
from app.schemas.projects import StartSessionRequest

# In-memory session store (mock)
sessions: Dict[str, Dict] = {}

def start_session(mode: str) -> str:
    """
    Start a new session and store it in memory.
    Called by: /api/v1/projects/start endpoint
    Handles: Mode 1 Step 1 and Mode 2 Step 1

    Input:
        - mode: "video" or "game"

    Output:
        - session_id: Unique identifier for the new session
    """
    session_id = str(uuid.uuid4())
    sessions[session_id] = {
        "mode": mode,
        "story_steps": [],
        "game_rounds": [],
        "tasks": [],
        "created_at": "2025-11-27T12:00:00"  # Mock timestamp
    }
    return session_id
