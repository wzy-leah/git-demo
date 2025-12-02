import requests
import json
import base64

# 请替换为你的阿里云 DashScope API Key
# 确保这个 Key 有访问文生图 (如通义万相) 服务的权限
DASHSCOPE_API_KEY = "sk-xxxxxxxxxxxxxxxx" 

class SDClient:
    def generate_image(self, prompt: str) -> str:
        """
        调用阿里云通义万相（或任何云端文生图服务）生成图片。
        
        Input: 
            - prompt: 故事生成器提供的图片描述提示词。
        Output: 
            - 图片的 URL 或 Base64 字符串。
        """
        # 阿里云通义万相的 API 端点
        url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {DASHSCOPE_API_KEY}"
        }
        
        # 构造请求体 (T2I 参数)
        payload = {
            "model": "wanx-v1",  # 使用通义万相模型
            "input": {
                "prompt": prompt
            },
            "parameters": {
                "n": 1,          # 生成一张图片
                "size": "1024*1024", # 图片尺寸 (按需调整)
                "style": "anime", # 风格 (可根据需求调整)
                "quality": "standard"
            }
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload)
            
            if response.status_code == 200:
                data = response.json()
                
                # 图像 API 通常返回一个包含 URL 的列表
                if data and data.get('output') and data['output'].get('results'):
                    # 返回第一个生成的图片的 URL
                    image_url = data['output']['results'][0]['url']
                    print(f"图片生成成功，URL: {image_url}")
                    return image_url
                else:
                    return "https://example.com/ai_image_generation_error.png" # 错误占位图
            else:
                print(f"图像 API 请求失败: {response.status_code} - {response.text}")
                return "https://example.com/api_connection_error.png"
                
        except Exception as e:
            print(f"图像 API 网络错误: {e}")
            return "https://example.com/network_error.png"

sd_client = SDClient()