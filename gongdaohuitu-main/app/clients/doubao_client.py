import requests
import json
import os

# 请替换为火山引擎 API Key 和 Model Endpoint ID
VOLC_API_KEY = os.getenv("VOLC_API_KEY")
DOUBAO_ENDPOINT_ID = os.getenv("DOUBAO_ENDPOINT_ID")

if not VOLC_API_KEY or not DOUBAO_ENDPOINT_ID:
    raise RuntimeError("豆包 VOLC_API_KEY 或 DOUBAO_ENDPOINT_ID 未配置，请在 .env 中设置")

class DoubaoClient:
    def _call_doubao(self, system_prompt: str, user_content: str) -> str:
        """通用调用方法"""
        url = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {VOLC_API_KEY}"
        }
        payload = {
            "model": DOUBAO_ENDPOINT_ID,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content}
            ]
        }
        try:
            response = requests.post(url, headers=headers, json=payload)
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"Error: {e}"

    def generate_game_tasks(self, image_description: str) -> list:
        """基于图片描述生成 3 个任务"""
        prompt = "基于以下图片描述，生成3个循序渐进的RPG游戏任务。请只返回JSON格式，包含id, description, difficulty。"
        result_text = self._call_doubao(prompt, image_description)
        # 这里需要加解析 JSON 的逻辑，简化起见直接返回文本或 mock 结构
        # 实际开发中建议用 json.loads(result_text)
        return [{"id": "1", "desc": result_text}] # 临时简化返回

    def score_story(self, full_story_text: str) -> dict:
        """对故事评分"""
        prompt = "请阅读以下故事，进行分析并打分（1-5星）。请以JSON格式返回：{stars: int, comment: str}。"
        result_text = self._call_doubao(prompt, full_story_text)
        return {"stars": 5, "comment": result_text} # 需解析 JSON

doubao_client = DoubaoClient()