from database.db import SessionLocal
from database.crud import insert_machine

db = SessionLocal()

try:
    machines = [
        ("CNC_001", "CNC Machine", "Factory Floor"),
        ("LATHE_001", "Lathe Machine", "Factory Floor"),
        ("DRILL_001", "Drill Press", "Workshop"),
        ("PRESS_001", "Hydraulic Press", "Assembly"),
        ("MILL_001", "Milling Machine", "Production"),
    ]

    for machine_id, name, location in machines:
        # Avoid inserting duplicates
        from database.crud import get_machine

        if get_machine(db, machine_id) is None:
            insert_machine(
                db=db,
                machine_id=machine_id,
                name=name,
                location=location,
            )

    print("Database seeded successfully!")

finally:
    db.close()