from datetime import datetime

from database.db import SessionLocal
from database.crud import (
    get_machine,
    insert_alarm,
    insert_cycle_event,
    insert_machine,
    insert_telemetry,
    insert_tool_change,
)

db = SessionLocal()

try:
    print("========== DATABASE SMOKE TEST ==========\n")

    # ----------------------------
    # Create machine (only if needed)
    # ----------------------------
    machine = get_machine(db, "TEST_001")

    if machine is None:
        machine = insert_machine(
            db=db,
            machine_id="TEST_001",
            name="Test CNC Machine",
            location="Testing Lab",
        )
        print("✅ Machine inserted")
    else:
        print("✅ Machine already exists")

    # ----------------------------
    # Insert telemetry
    # ----------------------------
    telemetry = insert_telemetry(
        db=db,
        machine_id="TEST_001",
        timestamp=datetime.now(),

        status="RUNNING",
        state="AUTOMATIC",

        program_id="P1001",
        tool_id=5,
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

    print("✅ Telemetry inserted")

    # ----------------------------
    # Insert alarm
    # ----------------------------
    alarm = insert_alarm(
        db=db,
        machine_id="TEST_001",

        timestamp=datetime.now(),
        alarm_code="ALM_101",
        message="Spindle temperature too high",
        severity="HIGH",
        status="ACTIVE",
        active=True,
    )

    print("✅ Alarm inserted")

    # ----------------------------
    # Insert tool change
    # ----------------------------
    tool_change = insert_tool_change(
        db=db,
        machine_id="TEST_001",

        timestamp=datetime.now(),
        tool_id=8,
        previous_tool_id=5,
        tool_offset=0.15,
        tool_wear=18.5,
        reason="Automatic Tool Change",
    )

    print("✅ Tool Change inserted")

    # ----------------------------
    # Insert cycle event
    # ----------------------------
    cycle_event = insert_cycle_event(
        db=db,
        machine_id="TEST_001",

        timestamp=datetime.now(),
        event="CYCLE_COMPLETE",
        cycle_id="CYCLE_001",
        program_id="P1001",
        tool_id=8,
        cycle_time_sec=24.8,
        part_number=125,
    )

    print("✅ Cycle Event inserted")

    print("\n🎉 ALL DATABASE TESTS PASSED SUCCESSFULLY!")

finally:
    db.close()