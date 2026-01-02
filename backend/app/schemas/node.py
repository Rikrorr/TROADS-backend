from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from uuid import UUID

class NodePosition(BaseModel):
    x: float
    y: float

class NodeData(BaseModel):
    question: Optional[str] = None
    answer: Optional[str] = None
    status: str
    superBlockId: str
    isLast: Optional[bool] = None
    label: Optional[str] = None

class NodeCreateRequest(BaseModel):
    position: NodePosition
    data: NodeData
    type: str = "chatNode"
    parentNode: Optional[str] = None

class NodeUpdateRequest(BaseModel):
    data: Dict[str, Any]

class NodeResponse(BaseModel):
    id: str
    type: str
    position: NodePosition
    data: NodeData
    parentNode: Optional[str] = None

    class Config:
        from_attributes = True
