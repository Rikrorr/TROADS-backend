# app/schemas.py
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

# --- 基础 ProjectData 结构 (对应前端 types.ts) ---
# 不需要严格校验每个 Node 的字段，因为 React Flow 的数据结构很深
# 使用 Dict[str, Any] 可以保持灵活性
class ProjectContent(BaseModel):
    version: str = "1.0.0"
    nodes: List[Dict[str, Any]] = []
    edges: List[Dict[str, Any]] = []
    viewport: Dict[str, Any] = {}

# --- 项目相关的 Schema ---
class ProjectCreate(BaseModel):
    name: str
    content: Optional[ProjectContent] = None

class ProjectResponse(BaseModel):
    id: int
    name: str
    content: ProjectContent
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True

# --- AI 对话相关的 Schema ---
class ChatRequest(BaseModel):
    model: str = "gpt-3.5-turbo"
    messages: List[Dict[str, str]]  # [{"role": "user", "content": "..."}]
    temperature: float = 0.7