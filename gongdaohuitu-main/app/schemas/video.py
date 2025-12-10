from pydantic import BaseModel
from typing import List, Optional

# --- 故事步骤模型 ---
class StoryStep(BaseModel):
    """定义故事中的每一步所需的数据结构"""
    image_url: str 
    prompt: str 

# --- 视频生成请求模型 ---
class GenerateVideoRequest(BaseModel):
    """请求 Schema：从故事步骤生成视频"""
    session_id: str
    mode: str 
    story_steps: List[StoryStep]
    duration: Optional[int] = None
    rhythm: Optional[str] = None

# --- 视频生成响应模型 ---
class GenerateVideoResponse(BaseModel):
    """
    响应 Schema：任务提交成功后返回的数据结构
    - 包含 task_id 用于轮询
    """
    session_id: str
    task_id: Optional[str] = None # 任务ID，用于前端轮询
    video_url: Optional[str] = None
    story_title: str
    cover_image_url: str
    audio_url: Optional[str] = None

# --- 视频状态查询请求模型 (轮询请求) ---
class QueryVideoRequest(BaseModel):
    """请求 Schema：根据任务ID查询视频生成状态"""
    task_id: str

# --- 视频状态查询响应模型 (轮询响应) ---
class QueryVideoResponse(BaseModel):
    """响应 Schema：查询视频生成状态的结果"""
    task_id: str
    status: str  # 任务状态，例如: "RUNNING", "COMPLETED", "FAILED"
    video_url: Optional[str] = None # 任务完成时返回URL
    check_count: Optional[int] = None # 方便调试，显示查询次数