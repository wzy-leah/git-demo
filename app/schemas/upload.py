from pydantic import BaseModel
from typing import List, Optional

class AnalyzeImageRequest(BaseModel):
    """
    Request schema for analyzing uploaded/drawn image
    Corresponding to:
    - Mode 1 Step 2: User completes upload/draw and clicks "Next: Recognize Image"
    - Mode 2 Step 2: User completes upload/draw and system analyzes image for game
    """
    session_id: str
    image_file: Optional[str] = None  # Base64 encoded image or URL
    image_url: Optional[str] = None  # Alternative: direct URL to image
    mode: str  # "video" or "game"

class AnalyzeImageResponseVideo(BaseModel):
    """
    Response schema for image analysis in video mode
    Corresponding to Mode 1 Step 2 output
    """
    session_id: str
    image_caption: str
    characters: List["Character"]  # List of manipulable characters
    suggestions: List[str]  # Style/worldview suggestions

class AnalyzeImageResponseGame(BaseModel):
    """
    Response schema for image analysis in game mode
    Corresponding to Mode 2 Step 2 output
    """
    session_id: str
    image_caption: str
    main_character: "Character"  # Selected main character for game

class Character(BaseModel):
    id: str
    name: str
    type: Optional[str] = None
    short_desc: str

AnalyzeImageResponseVideo.model_rebuild()
AnalyzeImageResponseGame.model_rebuild()
