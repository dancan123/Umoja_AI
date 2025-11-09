# app/main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.config import settings
from app.database import engine, Base
from app.routers import sample, chat

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="AI platform for Kenyan local languages"
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(sample.router, prefix="/api")
app.include_router(chat.router, prefix="/api")

# Create tables on startup
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Root endpoint
@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.app_name}!",
        "version": settings.app_version,
        "supported_languages": settings.supported_languages
    }