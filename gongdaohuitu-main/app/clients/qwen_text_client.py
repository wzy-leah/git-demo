import requests
import json

# =======================================================
# ⚠️ 关键参数：请替换为你的阿里云 DashScope API Key ⚠️
# =======================================================
DASHSCOPE_API_KEY = "sk-xxxxxxxxxxxxxxxx" 

class QwenTextClient:
    """Client for Qwen2 text generation service, connected to DashScope API"""

    def generate_response(self, messages: list, temperature: float = 0.8) -> str:
        """
        根据完整的对话历史生成回复。
        
        Input:
            - messages: 包含整个对话历史的列表，格式为 [{"role": "user", "content": "..."}, ...]
            - temperature: 控制模型生成随机性和创造性 (0.0 到 1.0)
            
        Output:
            - AI 生成的回复文本
        """
        if not DASHSCOPE_API_KEY or DASHSCOPE_API_KEY == "sk-xxxxxxxxxxxxxxxx":
             return "错误：Qwen API Key 未配置，无法调用 AI。"
             
        url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {DASHSCOPE_API_KEY}"
        }

        # 构造请求体
        body = {
            "model": "qwen-turbo", # 推荐使用 qwen-turbo 或 qwen-max
            "input": {
                "messages": messages
            },
            "parameters": {
                "temperature": temperature,
                "result_format": "message" # 返回结构化的消息格式
            }
        }

        try:
            response = requests.post(url, headers=headers, json=body)
            response.raise_for_status() # 检查 HTTP 错误，如果状态码不是 2xx 则抛出异常
            
            data = response.json()
            
            # 解析 AI 回复
            if data and data.get('output') and data['output'].get('choices'):
                ai_text = data['output']['choices'][0]['message']['content']
                return ai_text
            else:
                print("Qwen API 返回结构异常:", data)
                return "AI 服务返回了未知格式的回复。"
                
        except requests.exceptions.RequestException as e:
            # 处理网络连接或 HTTP 状态码错误
            print(f"Qwen API 调用失败: {e}")
            return "AI 服务连接失败，请检查 API Key 或网络连接。"

    # ⚠️ 注意：原有的 generate_story 和 continue_story 方法已被此通用的 generate_response 替代。
    # 在 services/story_service.py 或 game_service.py 中，只需要调用 generate_response
    # 并传入完整的历史消息列表即可实现故事的连贯生成。
    # 为了兼容旧代码，你也可以保留这两个函数，并让它们调用 generate_response。

qwen_text_client = QwenTextClient()