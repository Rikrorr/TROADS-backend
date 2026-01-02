from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.node import NodeResponse
from app.schemas.edge import EdgeResponse
from app.models.node import Node
from app.models.edge import Edge

router = APIRouter(prefix="/api/graph", tags=["graph"])


@router.get("", response_model=dict)
def get_graph_data(db: Session = Depends(get_db)):
    # 获取所有节点和边
    nodes = db.query(Node).all()
    edges = db.query(Edge).all()

    # 转换为前端需要的格式
    nodes_response = [
        NodeResponse(
            id=node.node_id,
            type=node.type,
            position=node.position,
            data=node.data,
            parentNode=node.parent_node
        )
        for node in nodes
    ]

    edges_response = [
        EdgeResponse(
            id=edge.edge_id,
            source=edge.source,
            target=edge.target,
            sourceHandle=edge.source_handle,
            targetHandle=edge.target_handle,
            type=edge.type,
            data=edge.data
        )
        for edge in edges
    ]

    return {
        "nodes": [node.dict() for node in nodes_response],
        "edges": [edge.dict() for edge in edges_response]
    }


@router.post("", response_model=dict)
def save_graph_data(data: dict, db: Session = Depends(get_db)):
    # 清除现有数据
    db.query(Edge).delete()
    db.query(Node).delete()

    # 保存新节点
    for node_data in data.get("nodes", []):
        node = Node(
            node_id=node_data["id"],
            type=node_data["type"],
            position=node_data["position"],
            data=node_data["data"],
            parent_node=node_data.get("parentNode")
        )
        db.add(node)

    # 保存新边
    for edge_data in data.get("edges", []):
        edge = Edge(
            edge_id=edge_data["id"],
            source=edge_data["source"],
            target=edge_data["target"],
            source_handle=edge_data.get("sourceHandle"),
            target_handle=edge_data.get("targetHandle"),
            type=edge_data["type"],
            data=edge_data.get("data")
        )
        db.add(edge)

    db.commit()
    return {"success": True}
