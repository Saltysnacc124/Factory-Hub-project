from models import MachineEvent


def create_machine_event(
    db,
    machine_name,
    status,
    spindle_rpm,
    feed_rate,
    spindle_load,
    spindle_temp,
    x_position,
    y_position,
    z_position,
    tool_id,
    tool_wear,
    current_cycle_time,
    cycle_duration,
    production_count,
    alarm_code,
    alarm_severity,
    alarm_message,
    event_type
):
    event = MachineEvent(
        machine_name=machine_name,
        status=status,
        spindle_rpm=spindle_rpm,
        feed_rate=feed_rate,
        spindle_load=spindle_load,
        spindle_temp=spindle_temp,
        x_position=x_position,
        y_position=y_position,
        z_position=z_position,
        tool_id=tool_id,
        tool_wear=tool_wear,
        current_cycle_time=current_cycle_time,
        cycle_duration=cycle_duration,
        production_count=production_count,
        alarm_code=alarm_code,
        alarm_severity=alarm_severity,
        alarm_message=alarm_message,
        event_type=event_type
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    return event
