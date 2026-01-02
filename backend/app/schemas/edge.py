from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from uuid import UUID

class EdgeData(BaseModel):
    controlPointOffset: Optional[Dict[str, float]] = None
    labels: Optional[List[Dict[str, Any]]] = None
    waypoints: Optional[List[Dict[str, float]]] = None
    isManual: Optional[bool] = None

class EdgeCreateRequest(BaseModel):
    source: str
    target: str
    sourceHandle: Optional[str] = None
    targetHandle: Optional[str] = None
    type: str = "editableEdge"
    data: Optional[EdgeData] = None

class EdgeUpdateRequest(BaseModel):
    data: Dict[str, Any]

class EdgeResponse(BaseModel):
    id: str
    source: str
    target: str
    sourceHandle: Optional[str] = None
    targetHandle: Optional[str] = None
    type: str
    data: Optional[EdgeData] = None

    class Config:
        from_attributes = True
