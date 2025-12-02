from app.schemas.interact import InitStoryRequest, UserFeedbackRequest
from app.clients.qwen_text_client import qwen_text_client
from app.clients.sd_client import sd_client

def init_story(request: InitStoryRequest) -> dict:
    """
    Initialize story generation with user-configured styles.
    Called by: /api/v1/interact/init-story endpoint
    Handles: Mode 1 Step 3

    Input:
        - request: InitStoryRequest object with user configurations

    Output:
        - Result dict with initial story step
    """
    # Mock result
    return {
        "session_id": request.session_id,
        "step_index": 0,
        "story_text": "Once upon a time, in a small village, there lived a brave knight named Arthur. He was known for his courage and kindness towards everyone. One day, a mysterious wizard visited the village with an important mission...",
        "image_url": "https://example.com/mock-image-1.jpg"
    }

def regenerate_image(request: UserFeedbackRequest) -> dict:
    """
    Regenerate image for current story step.
    Called by: /api/v1/interact/regenerate-image endpoint
    Handles: Mode 1 Step 4 - regenerate current image

    Input:
        - request: UserFeedbackRequest with step index and feedback

    Output:
        - Result dict with regenerated image URL
    """
    # Mock result
    return {
        "session_id": request.session_id,
        "step_index": request.step_index,
        "image_url": f"https://example.com/mock-image-{request.step_index}-regenerated.jpg"
    }

def next_step(request: UserFeedbackRequest) -> dict:
    """
    Generate next story step.
    Called by: /api/v1/interact/next-step endpoint
    Handles: Mode 1 Step 4 - generate next step

    Input:
        - request: UserFeedbackRequest with current step and feedback

    Output:
        - Result dict with next story step
    """
    # Mock result
    return {
        "session_id": request.session_id,
        "step_index": request.step_index + 1,
        "story_text": f"Arthur decided to accept the wizard's mission. Together, they set off on a journey to find the magical artifact that could save the kingdom. With each step, they faced new challenges and made new friends... (Step {request.step_index + 1})",
        "image_url": f"https://example.com/mock-image-{request.step_index + 1}.jpg"
    }
