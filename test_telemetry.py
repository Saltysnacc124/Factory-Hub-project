from datetime import datetime

from database.db import SessionLocal
from database.crud import insert_telemetry

db = SessionLocal()

try:
    telemetry = insert_telemetry(
        db=db,
        machine_id="CNC_001",
        timestamp=datetime.now(),

        status="RUNNING",
        state="AUTOMATIC",

        program_id="P1001",
        tool_id="T05",
        cycle_id="CYCLE_001",

        cycle_active=True,
        current_cycle_time=18.4,
        cycle_time_target=25.0,

        part_count=125,

        spindle_rpm=1800.0,
        feed_rate=450.0,

        axis_x=125.6,
        axis_y=42.3,
        axis_z=-18.5,

        spindle_load=62.8,
        x_load=25.4,
        y_load=21.7,
        z_load=19.9,

        spindle_temp=58.2,
        motor_temp=49.7,

        tool_wear=12.5,

        feed_override=100.0,
        spindle_override=100.0,
    )

    print("Telemetry inserted successfully!")
    print(telemetry.id)

finally:
    db.close()