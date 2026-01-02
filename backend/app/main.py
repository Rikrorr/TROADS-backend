from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import nodes, edges, graph
from app.database import engine
from app.models import node, edge, label  # 导入模型以创建表

# 创建数据库表
node.Base.metadata.create_all(bind=engine)
edge.Base.metadata.create_all(bind=engine)
label.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Troads Graph API",
    description="API for managing graph nodes, edges and labels for the Troads visual conversation editor",
    version="1.0.0"
)

# 允许跨域请求（前端开发时需要）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应限制为特定域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 包含路由
app.include_router(nodes.router)
app.include_router(edges.router)
app.include_router(graph.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Troads Graph API"}
