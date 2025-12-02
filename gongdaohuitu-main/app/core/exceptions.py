from fastapi import HTTPException, status

class DreamPainterException(Exception):
    """Base exception class for DreamPainter"""
    pass

class InvalidSessionException(DreamPainterException):
    """Raised when session is invalid or expired"""
    pass

class ImageAnalysisException(DreamPainterException):
    """Raised when image analysis fails"""
    pass

class StoryGenerationException(DreamPainterException):
    """Raised when story generation fails"""
    pass

class ImageGenerationException(DreamPainterException):
    """Raised when image generation fails"""
    pass

class VideoGenerationException(DreamPainterException):
    """Raised when video generation fails"""
    pass

class GameTaskException(DreamPainterException):
    """Raised when game task generation or processing fails"""
    pass

# FastAPI exception handlers (to be registered in main.py later if needed)
def invalid_session_handler(request, exc):
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Session not found or expired"
    )

def image_analysis_handler(request, exc):
    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Failed to analyze image"
    )
