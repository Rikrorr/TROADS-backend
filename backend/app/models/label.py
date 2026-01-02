from sqlalchemy import Column, String, Text, DateTime, JSON, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.mutable import MutableDict
import uuid
from datetime import datetime
from app.database import Base

class Label(Base):
    __tablename__ = "labels"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    label_id = Column(String, unique=True, index=True, nullable=False)  # 前端生成的标签ID
    edge_id = Column(String, nullable=False)  # 关联的边ID
    text = Column(Text, nullable=False)  # 标签文本
    offset_x = Column(JSON, nullable=False)  # 相对X偏移量
    offset_y = Column(JSON, nullable=False)  # 相对Y偏移量
    style = Column(MutableDict.as_mutable(JSON), nullable=True)  # 标签样式
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
