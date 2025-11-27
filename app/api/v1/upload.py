from fastapi import APIRouter, HTTPException
from app.schemas.upload import (
    AnalyzeImageRequest, AnalyzeImageResponseVideo, AnalyzeImageResponseGame
)
from app.services import upload_service

router = APIRouter()

@router.post("/analyze", responses={
    200: {
        "description": "Image analyzed successfully",
        "content": {
            "application/json": {
                "oneOf": [
                    {"$ref": "#/components/schemas/AnalyzeImageResponseVideo"},
                    {"$ref": "#/components/schemas/AnalyzeImageResponseGame"}
                ]
            }
        }
    }
})
async def analyze_image(request: AnalyzeImageRequest):
    """
    Analyze uploaded/drawn image to extract elements and characters.
    Corresponding to:
    - Mode 1 Step 2: User completes upload/draw and clicks "Next: Recognize Image"
    - Mode 2 Step 2: User completes upload/draw and system analyzes image for game

    Request:
        - session_id: Current session ID
        - image_file: Base64 encoded image (optional, use either this or image_url)
        - image_url: Direct URL to image (optional, use either this or image_file)
        - mode: "video" or "game"

    Response (video mode):
        - image_caption: Description of the image
        - characters: List of manipulable characters
        - suggestions: Style/worldview suggestions

    Response (game mode):
        - image_caption: Description of the image
        - main_character: Selected main character for the game
    """
    if not request.image_file and not request.image_url:
        raise HTTPException(status_code=400, detail="Either image_file or image_url must be provided")

    if request.mode not in ["video", "game"]:
        raise HTTPException(status_code=400, detail="Mode must be either 'video' or 'game'")

    result = upload_service.analyze_image(request)

    if request.mode == "video":
        return AnalyzeImageResponseVideo(**result)
    else:
        return AnalyzeImageResponseGame(**result)
