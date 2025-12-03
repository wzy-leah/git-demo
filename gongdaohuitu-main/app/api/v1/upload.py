from fastapi import APIRouter
from app.schemas.upload import AnalyzeImageRequest
from app.services.upload_service import analyze_image as analyze_image_service

router = APIRouter()

@router.post("/analyze")
async def analyze_image(req: AnalyzeImageRequest):
    """
    接收前端 JSON + base64 的图片分析请求
    """
    return analyze_image_service(req)
