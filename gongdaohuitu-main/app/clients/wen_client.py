import requests
import time
import os

# 复用 DashScope Key
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")

if not DASHSCOPE_API_KEY:
    raise RuntimeError("DASHSCOPE_API_KEY 未配置，请在 .env 中设置")

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
    def query_video_result(self, task_id: str) -> dict:
        """根据任务ID查询视频生成结果，返回状态和视频URL（如果成功）"""
        url = f"https://dashscope.aliyuncs.com/compatible-mode/v1/services/aigc/video-generation/img2video/{task_id}"
        headers = {"Authorization": f"Bearer {DASHSCOPE_API_KEY}"}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status() # 抛出非200状态码的异常
            result = response.json()
            
            # 简化返回
            status = result.get('output', {}).get('task_status')
            video_url = result.get('output', {}).get('video_list', [{}])[0].get('url')
            
            return {
                "status": status,
                "video_url": video_url
            }
        except Exception as e:
            print(f"Error querying video task {task_id}: {e}")
            return {"status": "FAILED", "error": str(e)}

wen_client = WenClient()