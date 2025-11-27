from app.schemas.upload import AnalyzeImageRequest
from app.clients.qwen_vl_client import qwen_vl_client

def analyze_image(request: AnalyzeImageRequest) -> dict:
    """
    Analyze image using Qwen-VL client (mock implementation).
    Called by: /api/v1/upload/analyze endpoint
    Handles: Mode 1 Step 2 and Mode 2 Step 2

    Input:
        - request: AnalyzeImageRequest object

    Output:
        - Result dict with analysis data, varies by mode
    """
    if request.mode == "video":
        # Mock result for video mode
        return {
            "session_id": request.session_id,
            "image_caption": "A small village with a brave knight and a mysterious wizard",
            "characters": [
                {"id": "char_1", "name": "Brave Knight", "type": "human", "short_desc": "A brave knight with a silver armor"},
                {"id": "char_2", "name": "Mysterious Wizard", "type": "human", "short_desc": "A wise wizard with a long beard"}
            ],
            "suggestions": ["Medieval fantasy", "Adventure", "Friendship story"]
        }
    else:
        # Mock result for game mode
        return {
            "session_id": request.session_id,
            "image_caption": "A brave explorer with a backpack in a jungle",
            "main_character": {"id": "char_1", "name": "Explorer", "type": "human", "short_desc": "A brave explorer looking for treasure"}
        }
