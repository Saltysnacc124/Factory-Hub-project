from db import SessionLocal
from models import Machine, MachineEvent

db = SessionLocal()

machine = Machine(
    machine_name="CNC01",
    machine_type="CNC"
)

event = MachineEvent(
    machine_name="CNC01",
    status="Running",
    temperature=65,
    production_count=120
)

db.add(machine)
db.add(event)

db.commit()

print("Data inserted successfully")
