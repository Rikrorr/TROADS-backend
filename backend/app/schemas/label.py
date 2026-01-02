from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from uuid import UUID

class LabelStyle(BaseModel):
    fontSize: Optional[int] = None
    color: Optional[str] = None
    backgroundColor: Optional[str] = None
    borderColor: Optional[str] = None
    borderWidth: Optional[int] = None

class EdgeLabelData(BaseModel):
    id: str
    text: str
    offsetX: float
    offsetY: float
    absoluteX: Optional[float] = None
    absoluteY: Optional[float] = None
    isSnapped: Optional[bool] = None
    style: Optional[LabelStyle] = None

class LabelCreateRequest(BaseModel):
    text: str
    offsetX: float
    offsetY: float
    style: Optional[LabelStyle] = None

class LabelUpdateRequest(BaseModel):
    text: Optional[str] = None
    offsetX: Optional[float] = None
    offsetY: Optional[float] = None
    style: Optional[LabelStyle] = None

class LabelResponse(BaseModel):
    id: str
    text: str
    offsetX: float
    offsetY: float
    style: Optional[LabelStyle] = None

    class Config:
        from_attributes = True
