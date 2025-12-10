import os
import json
import base64
import requests


# 从 .env 获取 Stable Diffusion API Key
SD_API_KEY = os.getenv("SD_API_KEY")

if not SD_API_KEY:
    raise RuntimeError("SD_API_KEY 未配置，请在 .env 中设置")

class SDClient:
    def generate_image(self, prompt: str) -> str:
        """
        调用 Stability.ai 的 Stable Diffusion API 生成图片。
        
        Input:
            - prompt: 文本提示词
        Output:
            - 图片的 URL 或 Base64 编码
        """

        # Stable Diffusion 官方 API 地址
        url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

        headers = {
            "Authorization": f"Bearer {SD_API_KEY}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        # 官方推荐的请求体格式
        payload = {
            "text_prompts": [
                {"text": prompt}
            ],
            "cfg_scale": 7,           # 控制提示词强度
            "clip_guidance_preset": "FAST_BLUE",
            "samples": 1,             # 生成 1 张图片
            "steps": 30,              # 迭代步数（越大越清晰）
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code != 200:
                print(f"图像生成失败: {response.status_code} - {response.text}")
                return "https://example.com/api_error.png"

            data = response.json()

            # API 返回的是 Base64 编码的图片
            if data and "artifacts" in data:
                base64_image = data["artifacts"][0]["base64"]

                # 保存图片到本地（可选）
                os.makedirs("outputs", exist_ok=True)
                output_path = os.path.join("outputs", "sd_result.png")
                with open(output_path, "wb") as f:
                    f.write(base64.b64decode(base64_image))

                print(f"图片已生成并保存：{output_path}")
                # 你也可以返回 base64 数据给前端展示
                return f"data:image/png;base64,{base64_image}"

            else:
                print("返回数据异常，未找到图片。")
                return "https://example.com/no_image.png"

        except Exception as e:
            print(f"网络错误: {e}")
            return "https://example.com/network_error.png"


# 实例化客户端
sd_client = SDClient()
