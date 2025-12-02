from fastapi import APIRouter
from app.api.v1 import projects, upload, interact, video

router = APIRouter()

# Include all sub-routers
router.include_router(projects.router, prefix="/projects", tags=["projects"])
router.include_router(upload.router, prefix="/upload", tags=["upload"])
router.include_router(interact.router, prefix="/interact", tags=["interact"])
router.include_router(video.router, prefix="/video", tags=["video"])
