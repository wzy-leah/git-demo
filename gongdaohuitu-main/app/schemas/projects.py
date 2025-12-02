from pydantic import BaseModel
from typing import Optional

class StartSessionRequest(BaseModel):
    """
    Request schema for starting a new session (mode selection)
    Corresponding to:
    - Mode 1 Step 1: User selects mode and clicks "Start Creation"
    - Mode 2 Step 1: User selects game mode and clicks "Start Game"
    """
    mode: str  # Must be "video" or "game"

class StartSessionResponse(BaseModel):
    """Response schema for session creation"""
    session_id: str
    message: str
