from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # <--- 1. 新增导入
from app.api.v1.router import router as v1_router

app = FastAPI(
    title="DreamPainter Backend API",
    version="1.0.0",
    description="Backend for DreamPainter - Story Video Generator and Interactive Game"
)

# --- 2. 新增 CORS 配置 (解决 405 错误的关键) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # 允许任何前端地址 (比如你的 localhost:5500)
    allow_credentials=True,
    allow_methods=["*"],     # 允许任何方法 (GET, POST, OPTIONS 等)
    allow_headers=["*"],     # 允许任何请求头
)
# ---------------------------------------------

# Mount API v1
app.include_router(v1_router, prefix="/api/v1")

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to DreamPainter Backend API!"}
