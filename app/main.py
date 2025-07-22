from fastapi import FastAPI
from app.controller.v1.routes import api_router
from app.context.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME} API version {settings.VERSION}"}