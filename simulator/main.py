import json
import time
import paho.mqtt.client as mqtt

from cnc_machine import CNCMachine

machine = CNCMachine()

client = mqtt.Client()

client.connect(
    host="localhost",
    port=1883
)

client.loop_start()

while True:

    telemetry = machine.generate_telemetry()

    cycle_event = machine.generate_cycle_event()

    tool_change = machine.generate_tool_change()

    alarm = machine.generate_alarm()

    client.publish(
        topic=f"cnc/{machine.machine_id}/telemetry",
        payload=json.dumps(telemetry)
    )
    print("Published telemetry")

    if alarm is not None:

        client.publish(
            topic=f"cnc/{machine.machine_id}/alarm",
            payload=json.dumps(alarm)
        )
        print("Published alarm")

    if cycle_event is not None:

        client.publish(
            topic=f"cnc/{machine.machine_id}/cycle_event",
            payload=json.dumps(cycle_event)
        )
        print("Published cycle event")

    if tool_change is not None:

        client.publish(
            topic=f"cnc/{machine.machine_id}/tool_change",
            payload=json.dumps(tool_change)
        )
        print("Published tool change")

    machine.update()

    time.sleep(1)