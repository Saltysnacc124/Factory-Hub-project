from sqlalchemy.orm import Session

from database.models import (
    Machine,
    Telemetry,
    Alarm,
    ToolChange,
    CycleEvent,
)


# =========================
# MACHINE CRUD
# =========================

def insert_machine(
    db: Session,
    machine_id: str,
    name: str = None,
    location: str = None,
):
    machine = Machine(
        machine_id=machine_id,
        name=name,
        location=location,
    )

    db.add(machine)
    db.commit()
    db.refresh(machine)

    return machine


def get_machine(db: Session, machine_id: str):
    return (
        db.query(Machine)
        .filter(Machine.machine_id == machine_id)
        .first()
    )


def get_all_machines(db: Session):
    return db.query(Machine).all()


def delete_machine(db: Session, machine_id: str):
    machine = get_machine(db, machine_id)

    if machine:
        db.delete(machine)
        db.commit()

    return machine


# =========================
# TELEMETRY CRUD
# =========================

def insert_telemetry(db: Session, **kwargs):
    telemetry = Telemetry(**kwargs)

    db.add(telemetry)
    db.commit()
    db.refresh(telemetry)

    return telemetry


def get_machine_telemetry(db: Session, machine_id: str):
    return (
        db.query(Telemetry)
        .filter(Telemetry.machine_id == machine_id)
        .all()
    )


def get_latest_telemetry(db: Session, machine_id: str):
    return (
        db.query(Telemetry)
        .filter(Telemetry.machine_id == machine_id)
        .order_by(Telemetry.timestamp.desc())
        .first()
    )


def delete_telemetry(db: Session, telemetry_id: int):
    telemetry = (
        db.query(Telemetry)
        .filter(Telemetry.id == telemetry_id)
        .first()
    )

    if telemetry:
        db.delete(telemetry)
        db.commit()

    return telemetry


# =========================
# ALARM CRUD
# =========================

def insert_alarm(db: Session, **kwargs):
    alarm = Alarm(**kwargs)

    db.add(alarm)
    db.commit()
    db.refresh(alarm)

    return alarm


def get_machine_alarms(db: Session, machine_id: str):
    return (
        db.query(Alarm)
        .filter(Alarm.machine_id == machine_id)
        .all()
    )


def get_active_alarms(db: Session, machine_id: str):
    return (
        db.query(Alarm)
        .filter(
            Alarm.machine_id == machine_id,
            Alarm.active.is_(True)
        )
        .all()
    )


def delete_alarm(db: Session, alarm_id: int):
    alarm = (
        db.query(Alarm)
        .filter(Alarm.id == alarm_id)
        .first()
    )

    if alarm:
        db.delete(alarm)
        db.commit()

    return alarm


# =========================
# TOOL CHANGE CRUD
# =========================

def insert_tool_change(db: Session, **kwargs):
    tool_change = ToolChange(**kwargs)

    db.add(tool_change)
    db.commit()
    db.refresh(tool_change)

    return tool_change


def get_tool_changes(db: Session, machine_id: str):
    return (
        db.query(ToolChange)
        .filter(ToolChange.machine_id == machine_id)
        .all()
    )


def delete_tool_change(db: Session, tool_change_id: int):
    tool_change = (
        db.query(ToolChange)
        .filter(ToolChange.id == tool_change_id)
        .first()
    )

    if tool_change:
        db.delete(tool_change)
        db.commit()

    return tool_change


# =========================
# CYCLE EVENT CRUD
# =========================

def insert_cycle_event(db: Session, **kwargs):
    cycle_event = CycleEvent(**kwargs)

    db.add(cycle_event)
    db.commit()
    db.refresh(cycle_event)

    return cycle_event


def get_cycle_events(db: Session, machine_id: str):
    return (
        db.query(CycleEvent)
        .filter(CycleEvent.machine_id == machine_id)
        .all()
    )


def delete_cycle_event(db: Session, cycle_event_id: int):
    cycle_event = (
        db.query(CycleEvent)
        .filter(CycleEvent.id == cycle_event_id)
        .first()
    )

    if cycle_event:
        db.delete(cycle_event)
        db.commit()

    return cycle_event
