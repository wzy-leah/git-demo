from pydantic import BaseModel
from typing import List, Optional, Any

class SessionBase(BaseModel):
    """Base schema for session data"""
    mode: str  # "video" or "game"

class CharacterBase(BaseModel):
    """Base schema for character data"""
    id: str
    name: str
    type: Optional[str] = None
    short_desc: str
    style: Optional[str] = None  # User-provided style/character

class TaskBase(BaseModel):
    """Base schema for game task"""
    id: str
    description: str
    target_state: str
    difficulty: str  # "easy", "medium", "hard"

class StoryStepBase(BaseModel):
    """Base schema for story step in mode 1"""
    step_index: int
    story_text: str
    image_url: str
