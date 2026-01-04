# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 这里的 URL 需要改成你本地 PostgreSQL 的配置
# 格式: postgresql://用户名:密码@localhost:端口/数据库名
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456@localhost:5432/troads_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# 依赖项：获取 DB 会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()