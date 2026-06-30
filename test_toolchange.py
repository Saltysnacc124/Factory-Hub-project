from datetime import datetime

from database.db import SessionLocal
from database.crud import insert_tool_change

db = SessionLocal()

try:
    tool = insert_tool_change(
        db=db,
        machine_id="CNC_001",

        timestamp=datetime.now(),
        tool_id="T08",
        previous_tool_id="T05",
        tool_offset=0.15,
        tool_wear=18.5,
        reason="Automatic Tool Change",
    )

    print("Tool Change inserted!")
    print(tool.id)

finally:
    db.close()