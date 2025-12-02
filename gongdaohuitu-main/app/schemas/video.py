from pydantic import BaseModel
from typing import List, Optional

class GenerateVideoRequest(BaseModel):
    """
    Request schema for generating video from story steps
    Corresponding to:
    - Mode 1 Step 5: User clicks "End creation and generate video"
    - Mode 2 Step 6: User clicks "Generate complete story video"
    """
    session_id: str
    mode: str  # "video" or "game"
    duration: Optional[int] = None  # Total video duration in seconds
    rhythm: Optional[str] = None  # "fast", "medium", "slow"

class GenerateVideoResponse(BaseModel):
    """Response schema for generated video"""
    session_id: str
    video_url: str
    story_title: str
    cover_image_url: str
