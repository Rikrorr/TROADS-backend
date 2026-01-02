from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import uuid
from app.database import get_db
from app.schemas.edge import EdgeCreateRequest, EdgeUpdateRequest, EdgeResponse
from app.models.edge import Edge

router = APIRouter(prefix="/api/edges", tags=["edges"])


@router.post("", response_model=EdgeResponse)
def create_edge(edge_data: EdgeCreateRequest, db: Session = Depends(get_db)):
    db_edge = Edge(
        edge_id=str(uuid.uuid4()),
        source=edge_data.source,
        target=edge_data.target,
        source_handle=edge_data.sourceHandle,
        target_handle=edge_data.targetHandle,
        type=edge_data.type,
        data=edge_data.data.dict() if edge_data.data else None
    )
    db.add(db_edge)
    db.commit()
    db.refresh(db_edge)

    return EdgeResponse(
        id=db_edge.edge_id,
        source=db_edge.source,
        target=db_edge.target,
        sourceHandle=db_edge.source_handle,
        targetHandle=db_edge.target_handle,
        type=db_edge.type,
        data=db_edge.data
    )


@router.put("/{edge_id}", response_model=EdgeResponse)
def update_edge(edge_id: str, update_data: EdgeUpdateRequest, db: Session = Depends(get_db)):
    db_edge = db.query(Edge).filter(Edge.edge_id == edge_id).first()
    if not db_edge:
        raise HTTPException(status_code=404, detail="Edge not found")

    # 更新边数据
    for key, value in update_data.data.items():
        if db_edge.data:
            db_edge.data[key] = value
        else:
            db_edge.data = {key: value}

    db.commit()
    db.refresh(db_edge)

    return EdgeResponse(
        id=db_edge.edge_id,
        source=db_edge.source,
        target=db_edge.target,
        sourceHandle=db_edge.source_handle,
        targetHandle=db_edge.target_handle,
        type=db_edge.type,
        data=db_edge.data
    )


@router.delete("", response_model=dict)
def delete_edges(ids: List[str], db: Session = Depends(get_db)):
    db.query(Edge).filter(Edge.edge_id.in_(ids)).delete()
    db.commit()
    return {"success": True}
