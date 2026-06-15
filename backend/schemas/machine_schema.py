from pydantic import BaseModel


class MachineResponse(BaseModel):
    id: int
    name: str
    type: str