import os
import base64
import time
import hashlib
import hmac
import json
from urllib.parse import urlencode, urlparse

# 从 .env 中读取讯飞语音合成参数
XFYUN_TTS_APPID = os.getenv("XFYUN_TTS_APPID", "50366e55")
XFYUN_TTS_API_KEY = os.getenv("XFYUN_TTS_API_KEY", "f062b056faaeef60cf394342b6ea61f3")
XFYUN_TTS_API_SECRET = os.getenv("XFYUN_TTS_API_SECRET", "YjFmYWZlYThlMjY5MmU4OWQ3YmUwMWQ1")

TTS_API_HOST = "tts-api.xfyun.cn"
TTS_API_URL = "wss://tts-api.xfyun.cn/v2/tts"

if not XFYUN_TTS_APPID or not XFYUN_TTS_API_KEY or not XFYUN_TTS_API_SECRET:
    raise RuntimeError("讯飞语音合成 TTS 参数未配置，请在 .env 中设置 XFYUN_TTS_* 环境变量")

class TTSClient:
    """讯飞 TTS 客户端：将文字转为语音 Base64 或 URL"""

    def _create_auth_url(self, api_url: str) -> str:
        """生成带鉴权参数的 WebSocket URL"""
        # 获取当前 GMT 时间
        date = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())

        # 构造签名原文
        signature_origin = (
            f"host: {TTS_API_HOST}\n"
            f"date: {date}\n"
            f"GET /v2/tts HTTP/1.1"
        )

        # HMAC-SHA256 签名
        signature_sha = hmac.new(
            XFYUN_TTS_API_SECRET.encode("utf-8"),
            signature_origin.encode("utf-8"),
            digestmod=hashlib.sha256,
        ).digest()
        signature_b64 = base64.b64encode(signature_sha).decode("utf-8")

        authorization_origin = (
            f'api_key="{XFYUN_TTS_API_KEY}", algorithm="hmac-sha256", '
            f'headers="host date request-line", signature="{signature_b64}"'
        )
        authorization = base64.b64encode(authorization_origin.encode("utf-8")).decode("utf-8")

        # 组合为完整鉴权 URL
        v = urlparse(api_url)
        auth_url = (
            f"{v.scheme}://{v.netloc}{v.path}"
            f"?authorization={authorization}&date={date}&host={TTS_API_HOST}"
        )
        return auth_url

    def text_to_speech(self, text: str) -> str:
        """
        将文字转换为音频流。
        🚨 简化版：这里只返回 mock URL，实际应通过 websocket 取音频。
        """
        auth_url = self._create_auth_url(TTS_API_URL)
        print(f"✅ 鉴权 URL 生成成功：{auth_url}")

        # 这里省略实际 WebSocket 部分（推荐用 websocket-client 库实现）
        # 可参考讯飞官方 demo 获取 Base64 音频流
        # 暂时返回一个 mock URL
        audio_url = f"https://your-server.com/audio/{hashlib.md5(text.encode()).hexdigest()}.mp3"
        print(f"🔊 语音生成任务模拟完成：{audio_url}")
        return audio_url


tts_client = TTSClient()
