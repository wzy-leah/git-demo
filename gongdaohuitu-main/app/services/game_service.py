from app.schemas.interact import GenerateTasksRequest, GameStepRequest, AnalyzeStoryRequest
from app.clients.doubao_client import doubao_client
from app.clients.qwen_text_client import qwen_text_client
from app.clients.sd_client import sd_client

def generate_tasks(request: GenerateTasksRequest) -> dict:
    """
    Generate game tasks for mode 2.
    Called by: /api/v1/interact/generate-tasks endpoint
    Handles: Mode 2 Step 3

    Input:
        - request: GenerateTasksRequest with session ID

    Output:
        - Result dict with 3 generated tasks
    """
    # Mock result - 3 tasks as specified in requirements
    return {
        "session_id": request.session_id,
        "tasks": [
            {
                "id": "task_1",
                "description": "Find the hidden treasure map in the jungle",
                "target_state": "Successfully locate the treasure map",
                "difficulty": "easy"
            },
            {
                "id": "task_2",
                "description": "Cross the rickety bridge over the river",
                "target_state": "Successfully cross the river using the bridge",
                "difficulty": "medium"
            },
            {
                "id": "task_3",
                "description": "Defeat the guardian and claim the treasure",
                "target_state": "Successfully defeat the guardian and retrieve the treasure",
                "difficulty": "hard"
            }
        ]
    }

from app.schemas.interact import GenerateTasksRequest, GameStepRequest, AnalyzeStoryRequest
# 引入我们刚才改好的两个文件
from app.clients.qwen_text_client import qwen_text_client
from app.services.project_service import get_chat_history, append_chat_message

# ... (generate_tasks 函数保持不变) ...

def game_step(request: GameStepRequest) -> dict:
    """
    处理游戏回合：用户输入 -> 读取历史 -> AI生成 -> 保存历史 -> 返回前端
    """
    session_id = request.session_id
    player_action = request.player_action
    
    print(f"收到用户输入 (Round {request.round_index}): {player_action}")

    # 1. 把用户的这句话存进记忆
    append_chat_message(session_id, "user", player_action)

    # 2. 读取完整的历史记忆 (包含之前所有的对话)
    history = get_chat_history(session_id)
    
    # 可以在这里加一个系统提示词 (System Prompt) 设定 AI 的人设
    system_prompt = {"role": "system", "content": "你是一个RPG游戏的主持人。请根据玩家的行动简短地描述结果，并推动剧情发展。"}
    full_messages = [system_prompt] + history

    # 3. 把整个历史发给 AI，获取回复
    ai_response = qwen_text_client.generate_response(full_messages)
    
    # 4. 把 AI 的回复也存进记忆
    append_chat_message(session_id, "assistant", ai_response)

    # 5. 返回给前端
    # Mock task_status (如果你暂时还没做任务逻辑，这里可以先Mock)
    task_status = {
        "task_1": request.round_index >= 3, 
        "task_2": request.round_index >= 6, 
        "task_3": request.round_index >= 10
    }

    return {
        "session_id": session_id,
        "system_reaction_text": ai_response,  # 这里现在是真正的 AI 回复了！
        "image_url": f"https://example.com/mock-game-image-{request.round_index}.jpg", # 图片暂时还用Mock URL，下一步再修图片
        "task_status": task_status,
        "current_round": request.round_index
    }

# ... (analyze_story 函数保持不变) ...

def analyze_story(request: AnalyzeStoryRequest) -> dict:
    """
    Analyze completed story and generate rating.
    Called by: /api/v1/interact/analyze-story endpoint
    Handles: Mode 2 Step 7

    Input:
        - request: AnalyzeStoryRequest with session ID

    Output:
        - Result dict with rating and analysis
    """
    # Mock result - random rating for demonstration
    return {
        "stars": 3,
        "comment": "Your story shows great courage and determination! You successfully completed all 3 tasks with clever thinking and bravery. The narrative flows well and the character development is strong.",
        "story_type": "Adventure"
    }
