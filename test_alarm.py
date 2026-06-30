from datetime import datetime

from database.db import SessionLocal
from database.crud import insert_alarm

db = SessionLocal()

try:
    alarm = insert_alarm(
        db=db,
        machine_id="CNC_001",

        timestamp=datetime.now(),
        alarm_code="ALM_101",
        message="Spindle temperature too high",
        severity="HIGH",
        status="ACTIVE",
        active=True,
    )

    print("Alarm inserted!")
    print(alarm.id)

finally:
    db.close()