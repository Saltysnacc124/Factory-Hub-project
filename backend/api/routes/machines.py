from fastapi import APIRouter

router = APIRouter(
    prefix="/machines",
    tags=["Machines"]
)

@router.get("/")
def get_machines():
    return [
        {
            "id": 1,
            "name": "CNC01",
            "type": "CNC"
        },
        {
            "id": 2,
            "name": "PRESS01",
            "type": "Press"
        }
    ]