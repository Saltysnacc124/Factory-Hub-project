from datetime import datetime

from database.db import SessionLocal
from database.crud import insert_cycle_event

db = SessionLocal()

try:
    cycle = insert_cycle_event(
        db=db,
        machine_id="CNC_001",

        timestamp=datetime.now(),
        event="CYCLE_COMPLETE",
        cycle_id="CYCLE_001",
        program_id="P1001",
        tool_id="T08",
        cycle_time_sec=24.8,
        part_number="PART_125",
    )

    print("Cycle Event inserted!")
    print(cycle.id)

finally:
    db.close()