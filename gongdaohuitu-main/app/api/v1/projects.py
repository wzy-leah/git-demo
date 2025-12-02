from fastapi import APIRouter, HTTPException
from app.schemas.projects import StartSessionRequest, StartSessionResponse
from app.services import project_service

router = APIRouter()

@router.post("/start", response_model=StartSessionResponse)
async def start_session(request: StartSessionRequest):
    """
    Start a new session for either video generation or game mode.
    Corresponding to:
    - Mode 1 Step 1: User selects video mode and clicks "Start Creation"
    - Mode 2 Step 1: User selects game mode and clicks "Start Game"

    Request:
        - mode: "video" or "game"

    Response:
        - session_id: Unique identifier for the session
        - message: Success message
    """
    if request.mode not in ["video", "game"]:
        raise HTTPException(status_code=400, detail="Mode must be either 'video' or 'game'")

    session_id = project_service.start_session(request.mode)
    return StartSessionResponse(session_id=session_id, message="Session created successfully")
