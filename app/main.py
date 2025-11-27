from fastapi import FastAPI
from app.api.v1.router import router as v1_router

app = FastAPI(
    title="DreamPainter Backend API",
    version="1.0.0",
    description="Backend for DreamPainter - Story Video Generator and Interactive Game"
)

# Mount API v1
app.include_router(v1_router, prefix="/api/v1")

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to DreamPainter Backend API!"}
