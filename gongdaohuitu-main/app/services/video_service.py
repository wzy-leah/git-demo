import uuid
from typing import Optional
from app.schemas.video import GenerateVideoRequest, GenerateVideoResponse, QueryVideoRequest, QueryVideoResponse
from app.clients.wen_client import wen_client
from app.clients.tts_client import tts_client
from app.clients.qwen_text_client import qwen_text_client

# 临时存储任务状态的 Mock 字典 (用于模拟任务进度)
MOCK_TASK_STORE = {}

# ----------------------------------------------------
# 1. 视频生成服务 (Generate Video)
# ----------------------------------------------------

def generate_video(request: GenerateVideoRequest) -> dict:
    """Submits the video generation task and returns a task ID."""
    
    if not request.story_steps:
        raise ValueError("Cannot generate video without story steps. 'story_steps' is empty.")
        
    last_step = request.story_steps[-1]
    image_url_to_use = last_step.image_url
    prompt_to_use = last_step.prompt
    
    print(f"INFO: Submitting video generation task for session {request.session_id}...")
    
    try:
        # Assuming wen_client.generate_video returns the task ID string
        video_task_id = wen_client.generate_video(
            image_url=image_url_to_use, 
            prompt=prompt_to_use
        )
    except Exception as e:
        print(f"ERROR: WenClient call failed: {e}")
        # Use a mock ID if the client call fails, for continued testing
        video_task_id = str(uuid.uuid4())
        print(f"WARNING: Using mock task ID {video_task_id} due to client error.")

    return {
        "session_id": request.session_id,
        "task_id": video_task_id,
        "story_title": "Video Generation Task Submitted", 
        "cover_image_url": image_url_to_use, 
        "video_url": None,
        "audio_url": None
    }

# ----------------------------------------------------
# 2. 视频查询服务 (Query Video Result) - Mock Logic
# ----------------------------------------------------

def query_video_result(request: QueryVideoRequest) -> dict:
    """Queries the video generation result based on task ID and simulates polling completion."""
    task_id = request.task_id
    
    if task_id not in MOCK_TASK_STORE:
        MOCK_TASK_STORE[task_id] = {
            "status": "RUNNING",
            "check_count": 0,
            "video_url": None
        }

    task_data = MOCK_TASK_STORE[task_id]
    task_data["check_count"] += 1
    
    # Simulate completion: Task completes after 3 checks
    if task_data["check_count"] >= 3 and task_data["status"] != "COMPLETED":
        task_data["status"] = "COMPLETED"
        # Simulate a final video URL
        task_data["video_url"] = f"https://mock.yourserver.com/videos/{task_id}_final.mp4"
        
        # ❗ CRITICAL: Print the final URL to the Uvicorn terminal
        print("-" * 50)
        print(f"✅✅✅ 任务 {task_id} 已模拟完成! ✅✅✅")
        print(f"📢 最终视频 URL (Mock): {task_data['video_url']}")
        print("-" * 50)
    
    return {
        "task_id": task_id,
        "status": task_data["status"],
        "check_count": task_data["check_count"],
        "video_url": task_data["video_url"]
    }