from app.schemas.interact import GenerateTasksRequest, GameStepRequest, AnalyzeStoryRequest
from app.clients.doubao_client import doubao_client
from app.clients.qwen_text_client import qwen_text_client
from app.clients.sd_client import sd_client

def generate_tasks(request: GenerateTasksRequest) -> dict:
    """
    Generate game tasks for mode 2.
    Called by: /api/v1/interact/generate-tasks endpoint
    Handles: Mode 2 Step 3

    Input:
        - request: GenerateTasksRequest with session ID

    Output:
        - Result dict with 3 generated tasks
    """
    # Mock result - 3 tasks as specified in requirements
    return {
        "session_id": request.session_id,
        "tasks": [
            {
                "id": "task_1",
                "description": "Find the hidden treasure map in the jungle",
                "target_state": "Successfully locate the treasure map",
                "difficulty": "easy"
            },
            {
                "id": "task_2",
                "description": "Cross the rickety bridge over the river",
                "target_state": "Successfully cross the river using the bridge",
                "difficulty": "medium"
            },
            {
                "id": "task_3",
                "description": "Defeat the guardian and claim the treasure",
                "target_state": "Successfully defeat the guardian and retrieve the treasure",
                "difficulty": "hard"
            }
        ]
    }

def game_step(request: GameStepRequest) -> dict:
    """
    Process game round and generate result.
    Called by: /api/v1/interact/game-step endpoint
    Handles: Mode 2 Step 5

    Input:
        - request: GameStepRequest with round index and player action

    Output:
        - Result dict with game round result
    """
    # Mock result - assume task status progress
    task_status = {"task_1": request.round_index >= 3, "task_2": request.round_index >= 6, "task_3": request.round_index >= 10}

    return {
        "session_id": request.session_id,
        "system_reaction_text": f"Round {request.round_index}: You decided to {request.player_action}. After a brave effort, you made progress. The path ahead looks challenging but rewarding!",
        "image_url": f"https://example.com/mock-game-image-{request.round_index}.jpg",
        "task_status": task_status,
        "current_round": request.round_index
    }

def analyze_story(request: AnalyzeStoryRequest) -> dict:
    """
    Analyze completed story and generate rating.
    Called by: /api/v1/interact/analyze-story endpoint
    Handles: Mode 2 Step 7

    Input:
        - request: AnalyzeStoryRequest with session ID

    Output:
        - Result dict with rating and analysis
    """
    # Mock result - random rating for demonstration
    return {
        "stars": 3,
        "comment": "Your story shows great courage and determination! You successfully completed all 3 tasks with clever thinking and bravery. The narrative flows well and the character development is strong.",
        "story_type": "Adventure"
    }
