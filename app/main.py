from fastapi import FastAPI
from app.context.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.get("/")
def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME} API version {settings.VERSION}"}