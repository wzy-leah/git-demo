from fastapi import APIRouter, HTTPException
from app.schemas.interact import (
    InitStoryRequest, InitStoryResponse, UserFeedbackRequest,
    RegenerateImageResponse, NextStepResponse, GenerateTasksRequest,
    GenerateTasksResponse, GameStepRequest, GameStepResponse,
    AnalyzeStoryRequest, AnalyzeStoryResponse
)
from app.services import story_service, game_service

router = APIRouter()

@router.post("/init-story", response_model=InitStoryResponse)
async def init_story(request: InitStoryRequest):
    """
    Initialize story generation with user-configured styles.
    Corresponding to Mode 1 Step 3: User configures styles and clicks "Generate first image and opening story"

    Request:
        - session_id: Current session ID
        - image_id: Image identifier (optional)
        - image_url: Image URL (optional)
        - characters: Characters with user-provided styles
        - story_style_input: Overall story style description

    Response:
        - step_index: Initial step index (0)
        - story_text: Opening story text
        - image_url: Generated first illustration
    """
    result = story_service.init_story(request)
    return InitStoryResponse(**result)

@router.post("/regenerate-image", response_model=RegenerateImageResponse)
async def regenerate_image(request: UserFeedbackRequest):
    """
    Regenerate image for current story step based on user feedback.
    Corresponding to Mode 1 Step 4: User clicks "Regenerate current image"

    Request:
        - session_id: Current session ID
        - step_index: Index of the step to regenerate
        - user_feedback: User's improvement suggestions

    Response:
        - step_index: Same step index
        - image_url: Regenerated image URL
    """
    result = story_service.regenerate_image(request)
    return RegenerateImageResponse(**result)

@router.post("/next-step", response_model=NextStepResponse)
async def next_step(request: UserFeedbackRequest):
    """
    Generate next story step based on user feedback.
    Corresponding to Mode 1 Step 4: User clicks "Generate next image and text"

    Request:
        - session_id: Current session ID
        - step_index: Index of the current step
        - user_feedback: User's improvement suggestions (optional)

    Response:
        - step_index: New step index
        - story_text: Next story segment
        - image_url: Generated next illustration
    """
    result = story_service.next_step(request)
    return NextStepResponse(**result)

@router.post("/generate-tasks", response_model=GenerateTasksResponse)
async def generate_tasks(request: GenerateTasksRequest):
    """
    Generate game tasks based on analyzed image.
    Corresponding to Mode 2 Step 3: User clicks "Generate Tasks"

    Request:
        - session_id: Current session ID

    Response:
        - tasks: List of 3 generated tasks
    """
    result = game_service.generate_tasks(request)
    return GenerateTasksResponse(**result)

@router.post("/game-step", response_model=GameStepResponse)
async def game_step(request: GameStepRequest):
    """
    Process game round action and generate result.
    Corresponding to Mode 2 Step 5: User submits action for current round

    Request:
        - session_id: Current session ID
        - round_index: Current round (1-10)
        - player_action: User's description of character's action

    Response:
        - system_reaction_text: System's reaction and story progress
        - image_url: Generated image for this round
        - task_status: Current completion status of all tasks
        - current_round: Same round index
    """
    if not 1 <= request.round_index <= 10:
        raise HTTPException(status_code=400, detail="Round index must be between 1 and 10")

    result = game_service.game_step(request)
    return GameStepResponse(**result)

@router.post("/analyze-story", response_model=AnalyzeStoryResponse)
async def analyze_story(request: AnalyzeStoryRequest):
    """
    Analyze completed story and provide rating.
    Corresponding to Mode 2 Step 7: User clicks "View Score"

    Request:
        - session_id: Current session ID

    Response:
        - stars: Rating (0-3 stars)
        - comment: Detailed evaluation
        - story_type: Type of story (e.g., "adventure", "healing")
    """
    result = game_service.analyze_story(request)
    return AnalyzeStoryResponse(**result)
