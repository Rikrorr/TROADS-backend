from sqlalchemy import Column, String, Text, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.mutable import MutableDict
import uuid
from datetime import datetime
from app.database import Base

class Node(Base):
    __tablename__ = "nodes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    node_id = Column(String, unique=True, index=True, nullable=False)  # 前端生成的节点ID
    type = Column(String, nullable=False)  # 'chatNode' 或 'groupNode'
    position = Column(MutableDict.as_mutable(JSON), nullable=False)  # {x: number, y: number}
    data = Column(MutableDict.as_mutable(JSON), nullable=False)  # 节点数据
    parent_node = Column(String, nullable=True)  # 父节点ID
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
