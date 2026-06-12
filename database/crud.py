from models import MachineEvent

def create_machine_event(db, machine_name, status, temperature, production_count):
    event = MachineEvent(
        machine_name=machine_name,
        status=status,
        temperature=temperature,
        production_count=production_count
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    return event
