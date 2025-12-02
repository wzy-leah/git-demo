import requests
import json

# 请替换为阿里云 API Key
DASHSCOPE_API_KEY = "sk-xxxxxxxxxxxxxxxx"

class QwenVLClient:
    def analyze_image(self, image_url_or_base64: str) -> str:
        """调用 Qwen-VL 识别图片内容"""
        url = "https://qwen-api.aliyun.com/v1"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {DASHSCOPE_API_KEY}"
        }
        
        # 构造多模态请求
        payload = {
            "model": "qwen-vl-max",
            "input": {
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {"image": image_url_or_base64}, # 支持 URL 或 Base64
                            {"text": "请详细描述这张图片中的场景、角色和氛围。"}
                        ]
                    }
                ]
            }
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 200:
                data = response.json()
                if "output" in data and "choices" in data["output"]:
                    return data["output"]["choices"][0]["message"]["content"][0]["text"]
            return "图片识别失败: " + response.text
        except Exception as e:
            return f"网络错误: {e}"

qwen_vl_client = QwenVLClient()