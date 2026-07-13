from fastapi import FastAPI

from app.api.v1.endpoints.photos import router as photo_router

app = FastAPI(
    title="Visual OS",
    version="0.1.0"
)

app.include_router(photo_router, prefix="/api/v1")


@app.get("/")
def root():
    return {
        "project": "Visual OS",
        "status": "running"
    }