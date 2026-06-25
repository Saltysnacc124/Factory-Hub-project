from fastapi import FastAPI

from backend.api.routes.machines import router
from mqtt.subscriber import start_subscriber

app = FastAPI(
    title="Factory Machine Data Hub"
)

app.include_router(router)


@app.on_event("startup")
def startup_event():
    start_subscriber()

    
@app.get("/")
def root():
    return {
        "message": "Factory Machine Data Hub",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }