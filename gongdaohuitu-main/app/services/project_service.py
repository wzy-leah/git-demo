from typing import Dict, List
import uuid
import datetime
from app.schemas.projects import StartSessionRequest

# 内存数据库 (注意：重启服务器后数据会丢失，测试阶段够用了)
sessions: Dict[str, Dict] = {}

def start_session(mode: str) -> str:
    """创建一个新会话"""
    session_id = str(uuid.uuid4())
    sessions[session_id] = {
        "mode": mode,
        "history": [],  # 专门用来存对话历史 [{"role": "user", "content": "..."}]
        "created_at": datetime.datetime.now().isoformat()
    }
    print(f"新会话已创建: {session_id}")
    return session_id

# --- 新增下面这两个函数，给 game_service 用 ---

def get_chat_history(session_id: str) -> List[Dict]:
    """获取指定会话的历史记录"""
    if session_id in sessions:
        return sessions[session_id]["history"]
    return []

def append_chat_message(session_id: str, role: str, content: str):
    """往历史记录里追加一条消息"""
    if session_id in sessions:
        sessions[session_id]["history"].append({
            "role": role,
            "content": content
        })