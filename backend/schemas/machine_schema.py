from typing import Optional
from pydantic import BaseModel


class MachineResponse(BaseModel):

    machine_id: str

    current_state: dict

    active_alarm: Optional[dict] = None

    current_tool: Optional[dict] = None

    last_cycle_event: Optional[dict] = None

    last_update: Optional[str] = None