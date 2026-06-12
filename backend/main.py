from fastapi import FastAPI
from backend.api.routes.machines import router

app = FastAPI()

app.include_router(router)