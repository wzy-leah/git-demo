from app.schemas.upload import AnalyzeImageRequest
from app.clients.qwen_vl_client import qwen_vl_client
import base64
import binascii
from fastapi import HTTPException

def analyze_image(request: AnalyzeImageRequest) -> dict:
    """
    Analyze image using Qwen-VL client (mock implementation).
    Called by: /api/v1/upload/analyze endpoint
    Handles: Mode 1 Step 2 and Mode 2 Step 2

    Input:
        - request: AnalyzeImageRequest object
            request.session_id: str
            request.image_file: base64 string (来自前端 JSON)
            request.image_url: 可选的图片 URL
            request.mode: "video" 或 "game"

    Output:
        - Result dict with analysis data, varies by mode
    """

    # 0. 基础校验：image_file / image_url 至少要有一个
    if not request.image_file and not request.image_url:
        raise HTTPException(status_code=400, detail="image_file or image_url is required")

    # 1. 从 base64 还原出图片的二进制 bytes（图片真正内容）
    image_bytes: bytes | None = None

    if request.image_file:
        try:
            # request.image_file 是前端传来的 base64 字符串
            image_bytes = base64.b64decode(request.image_file)
        except (ValueError, binascii.Error):
            # base64 格式不对
            raise HTTPException(status_code=400, detail="invalid base64 in image_file")
    else:
        # TODO：如果以后要支持 image_url，可以在这里下载图片
        # 比如用 httpx / requests 拉取，然后得到 image_bytes
        raise HTTPException(status_code=501, detail="image_url not implemented yet")

    # ============================================
    # 2. 在这里用 image_bytes 调用 Qwen-VL（暂时先保留 mock）
    #    以后你接真模型的时候，只要在这里换实现即可
    # ============================================

    # 示例：伪代码（根据你 qwen_vl_client 的实际接口来改）
    # vl_result = qwen_vl_client.analyze_image(
    #     image_bytes=image_bytes,
    #     mode=request.mode,
    # )

    # 现在我们先用你原来的 mock 逻辑，让前后端流程跑通：
    if request.mode == "video":
        # Mock result for video mode
        return {
            "session_id": request.session_id,
            "image_caption": "A small village with a brave knight and a mysterious wizard",
            "characters": [
                {
                    "id": "char_1",
                    "name": "Brave Knight",
                    "type": "human",
                    "short_desc": "A brave knight with a silver armor",
                },
                {
                    "id": "char_2",
                    "name": "Mysterious Wizard",
                    "type": "human",
                    "short_desc": "A wise wizard with a long beard",
                },
            ],
            "suggestions": ["Medieval fantasy", "Adventure", "Friendship story"],
        }
    else:
        # Mock result for game mode
        return {
            "session_id": request.session_id,
            "image_caption": "A brave explorer with a backpack in a jungle",
            "main_character": {
                "id": "char_1",
                "name": "Explorer",
                "type": "human",
                "short_desc": "A brave explorer looking for treasure",
            },
        }

