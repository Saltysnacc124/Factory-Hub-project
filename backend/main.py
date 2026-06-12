from fastapi import FastAPI
from backend.api.routes.machines import router

app = FastAPI(
    title="Factory Machine Data Hub"
)

app.include_router(router)

@app.get("/")
def root():
    return {
        "message": "Factory Hub",
        "machines_endpoint": "/machines/"
    }