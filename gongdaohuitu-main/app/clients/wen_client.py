import requests
import time

# 复用 DashScope Key
DASHSCOPE_API_KEY = "sk-xxxxxxxxxxxxxxxx"

class WenClient:
    def generate_video(self, image_url: str, prompt: str) -> str:
        """调用通义万相生成视频 (简化版)"""
        url = "https://dashscope.aliyuncs.com/compatible-mode/v1/services/aigc/video-generation/img2video"
        headers = {"Authorization": f"Bearer {DASHSCOPE_API_KEY}"}
        
        # 1. 提交任务
        payload = {
            "model": "wanx-v1",
            "input": {
                "image_url": image_url,
                "prompt": prompt
            }
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload)
            task_id = response.json().get('output', {}).get('task_id')
            
            # 2. (简化的逻辑) 实际项目中应该把 task_id 存库，由前端轮询
            # 这里为了演示，直接返回 task_id 或做个简单的等待提示
            return f"VIDEO_TASK_ID:{task_id}" 
            
        except Exception as e:
            return ""

wen_client = WenClient()
