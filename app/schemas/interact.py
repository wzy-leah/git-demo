from pydantic import BaseModel
from typing import List, Optional, Dict
from app.schemas.common import TaskBase, StoryStepBase

class InitStoryRequest(BaseModel):
    """
    Request schema for initial story generation in video mode
    Corresponding to Mode 1 Step 3: User configures styles and clicks "Generate first image and opening story"
    """
    session_id: str
    image_id: Optional[str] = None
    image_url: Optional[str] = None
    characters: List["CharacterConfig"]  # Characters with user-provided style
    story_style_input: str

class CharacterConfig(BaseModel):
    id: str
    style: str

class InitStoryResponse(BaseModel):
    """Response schema for initial story generation"""
    session_id: str
    step_index: int
    story_text: str
    image_url: str

class UserFeedbackRequest(BaseModel):
    """
    Request schema for user feedback during story generation
    Corresponding to Mode 1 Step 4: User provides feedback
    """
    session_id: str
    step_index: int
    user_feedback: Optional[str] = None  # User's improvement suggestions

class RegenerateImageResponse(BaseModel):
    """Response schema for regenerating an image"""
    session_id: str
    step_index: int
    image_url: str

class NextStepResponse(BaseModel):
    """Response schema for generating next story step"""
    session_id: str
    step_index: int
    story_text: str
    image_url: str

class GenerateTasksRequest(BaseModel):
    """
    Request schema for generating game tasks
    Corresponding to Mode 2 Step 3: User clicks "Generate Tasks"
    """
    session_id: str

class GenerateTasksResponse(BaseModel):
    """Response schema for generated game tasks"""
    session_id: str
    tasks: List[TaskBase]

class GameStepRequest(BaseModel):
    """
    Request schema for game round interaction
    Corresponding to Mode 2 Step 5: User submits action for current round
    """
    session_id: str
    round_index: int  # 1-10
    player_action: str

class GameStepResponse(BaseModel):
    """Response schema for game round result"""
    session_id: str
    system_reaction_text: str
    image_url: str
    task_status: Dict[str, bool]  # Task ID -> completion status
    current_round: int

class AnalyzeStoryRequest(BaseModel):
    """
    Request schema for story analysis and scoring in game mode
    Corresponding to Mode 2 Step 7: User clicks "View Score"
    """
    session_id: str

class AnalyzeStoryResponse(BaseModel):
    """Response schema for story analysis and scoring"""
    stars: int  # 0-3
    comment: str
    story_type: str  # e.g., "adventure", "healing"

# Rebuild models
InitStoryResponse.model_rebuild()
RegenerateImageResponse.model_rebuild()
NextStepResponse.model_rebuild()
GenerateTasksResponse.model_rebuild()
GameStepResponse.model_rebuild()
AnalyzeStoryResponse.model_rebuild()
