# app/routers/chat.py
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import time
import json

# 如果有真实 Key，可以使用 openai 库
# import openai

router = APIRouter()


class StreamRequest(BaseModel):
    nodeId: str
    question: str
    context: str = ""  # 上下文


@router.post("/stream")
async def stream_chat(req: StreamRequest):
    """
    模拟流式输出，或者调用真实的 OpenAI/Gemini API
    """

    async def event_generator():
        # 这里模拟 AI 思考和打字
        full_response = f"这里是后端返回的针对问题 '{req.question}' 的回答。\n\n我正在通过 FastAPI 的 StreamingResponse 逐字返回数据..."

        # 1. 模拟网络延迟
        yield f"data: {json.dumps({'status': 'loading'})}\n\n"
        time.sleep(0.5)

        # 2. 开始流式输出内容
        yield f"data: {json.dumps({'status': 'streaming', 'chunk': ''})}\n\n"

        for char in full_response:
            # 模拟打字机速度
            time.sleep(0.05)
            # SSE 格式: data: {...}\n\n
            data = json.dumps({"status": "streaming", "chunk": char})
            yield f"data: {data}\n\n"

        # 3. 结束
        yield f"data: {json.dumps({'status': 'completed'})}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")