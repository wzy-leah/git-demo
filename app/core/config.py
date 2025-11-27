from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """
    DreamPainter backend configuration settings
    """
    PROJECT_NAME: str = "DreamPainter"
    API_VERSION: str = "v1"
    DEBUG: bool = True

    # Mock configuration for clients
    MOCK_MODE: bool = True

    # Model endpoints (placeholder for future real API calls)
    QWEN_VL_ENDPOINT: str = "http://mock.qwen-vl.com/v1/analyze"
    QWEN_TEXT_ENDPOINT: str = "http://mock.qwen2.com/v1/completions"
    SD_ENDPOINT: str = "http://mock.sd.com/v1/generate"
    WEN_VIDEO_ENDPOINT: str = "http://mock.wen.com/v1/video"
    TTS_ENDPOINT: str = "http://mock.iflytek.com/v1/tts"
    DOBAO_ENDPOINT: str = "http://mock.doubao.com/v1/generate"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
