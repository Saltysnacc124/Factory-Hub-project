from typing import List

from fastapi import APIRouter

from backend.schemas.machine_schema import MachineResponse
from backend.services.machine_service import get_all_machines

router = APIRouter(
    prefix="/machines",
    tags=["Machines"]
)


@router.get("/", response_model=List[MachineResponse])
def get_machines():
    return get_all_machines()