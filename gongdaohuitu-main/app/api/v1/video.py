from fastapi import APIRouter, HTTPException
from app.schemas.video import GenerateVideoRequest, GenerateVideoResponse
from app.services import video_service

router = APIRouter()

@router.post("/generate", response_model=GenerateVideoResponse)
async def generate_video(request: GenerateVideoRequest):
    """
    Generate video from story steps.
    Corresponding to:
    - Mode 1 Step 5: User clicks "End creation and generate video"
    - Mode 2 Step 6: User clicks "Generate complete story video"

    Request:
        - session_id: Current session ID
        - mode: "video" or "game"
        - duration: Total video duration (optional)
        - rhythm: Video rhythm (optional: "fast", "medium", "slow")

    Response:
        - video_url: URL of generated video
        - story_title: Generated story title
        - cover_image_url: URL of cover image
    """
    if request.mode not in ["video", "game"]:
        raise HTTPException(status_code=400, detail="Mode must be either 'video' or 'game'")

    result = video_service.generate_video(request)
    return GenerateVideoResponse(**result)
