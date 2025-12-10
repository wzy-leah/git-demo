import asyncio
from fastapi import APIRouter
from app.schemas.video import GenerateVideoRequest, GenerateVideoResponse, QueryVideoRequest, QueryVideoResponse
from app.services import video_service

router = APIRouter()

@router.post("/generate", response_model=GenerateVideoResponse)
async def generate_video(request: GenerateVideoRequest):
    """提交视频生成任务"""
    result = await asyncio.to_thread(video_service.generate_video, request)
    return result

@router.post("/query-result", response_model=QueryVideoResponse)
async def query_video_result(request: QueryVideoRequest):
    """
    根据任务ID查询视频的生成状态和最终URL。
    这是前端轮询调用的接口。
    """
    result = await asyncio.to_thread(video_service.query_video_result, request)
    return result