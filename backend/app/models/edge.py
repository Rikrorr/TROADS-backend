from sqlalchemy import Column, String, Text, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.mutable import MutableDict
import uuid
from datetime import datetime
from app.database import Base

class Edge(Base):
    __tablename__ = "edges"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    edge_id = Column(String, unique=True, index=True, nullable=False)  # 前端生成的边ID
    source = Column(String, nullable=False)  # 源节点ID
    target = Column(String, nullable=False)  # 目标节点ID
    source_handle = Column(String, nullable=True)  # 源句柄ID
    target_handle = Column(String, nullable=True)  # 目标句柄ID
    type = Column(String, nullable=False)  # 'editableEdge'
    data = Column(MutableDict.as_mutable(JSON), nullable=True)  # 连线数据
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
