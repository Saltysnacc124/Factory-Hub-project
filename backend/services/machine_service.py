from backend.schemas.machine_schema import MachineResponse


def get_all_machines():
    return [
        MachineResponse(
            id=1,
            name="CNC01",
            type="CNC"
        ),
        MachineResponse(
            id=2,
            name="PRESS01",
            type="Press"
        )
    ]