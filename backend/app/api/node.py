from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import uuid
from app.database import get_db
from app.schemas.node import NodeCreateRequest, NodeUpdateRequest, NodeResponse
from app.models.node import Node

router = APIRouter(prefix="/api/nodes", tags=["nodes"])


@router.post("/chat", response_model=NodeResponse)
def create_chat_node(node_data: NodeCreateRequest, db: Session = Depends(get_db)):
    # 创建问答节点
    db_node = Node(
        node_id=str(uuid.uuid4()),
        type=node_data.type,
        position=node_data.position.dict(),
        data=node_data.data.dict(),
        parent_node=node_data.parentNode
    )
    db.add(db_node)
    db.commit()
    db.refresh(db_node)

    # 返回节点信息
    return NodeResponse(
        id=db_node.node_id,
        type=db_node.type,
        position=db_node.position,
        data=db_node.data,
        parentNode=db_node.parent_node
    )


@router.post("/group", response_model=NodeResponse)
def create_group_node(node_data: NodeCreateRequest, db: Session = Depends(get_db)):
    # 创建分组节点
    db_node = Node(
        node_id=str(uuid.uuid4()),
        type="groupNode",
        position=node_data.position.dict(),
        data=node_data.data.dict(),
        parent_node=node_data.parentNode
    )
    db.add(db_node)
    db.commit()
    db.refresh(db_node)

    return NodeResponse(
        id=db_node.node_id,
        type=db_node.type,
        position=db_node.position,
        data=db_node.data,
        parentNode=db_node.parent_node
    )


@router.put("/chat/{node_id}", response_model=NodeResponse)
def update_chat_node(node_id: str, update_data: NodeUpdateRequest, db: Session = Depends(get_db)):
    db_node = db.query(Node).filter(Node.node_id == node_id).first()
    if not db_node:
        raise HTTPException(status_code=404, detail="Node not found")

    # 更新节点数据
    for key, value in update_data.data.items():
        db_node.data[key] = value

    db.commit()
    db.refresh(db_node)

    return NodeResponse(
        id=db_node.node_id,
        type=db_node.type,
        position=db_node.position,
        data=db_node.data,
        parentNode=db_node.parent_node
    )


@router.delete("", response_model=dict)
def delete_nodes(ids: List[str], db: Session = Depends(get_db)):
    db.query(Node).filter(Node.node_id.in_(ids)).delete()
    db.commit()
    return {"success": True}
