from database.db import SessionLocal
from database.crud import insert_machine, get_machine

# Create a database session
db = SessionLocal()

try:
    # Insert a machine
    machine = insert_machine(
        db=db,
        machine_id="CNC001",
        name="Test CNC Machine",
        location="Factory Floor"
    )

    print("Machine inserted successfully!")
    print(machine.machine_id)

    # Read it back
    fetched_machine = get_machine(db, "CNC001")

    print("\nRetrieved from database:")
    print(f"Machine ID: {fetched_machine.machine_id}")
    print(f"Name: {fetched_machine.name}")
    print(f"Location: {fetched_machine.location}")

finally:
    db.close()