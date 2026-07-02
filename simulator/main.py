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

print("Simulation Modes:")
print("1. Continuous Mode")
print("2. Manual Mode")

mode = input("Select mode (1/2): ").strip()

def publish_one_cycle():

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


if mode == "1":
    while True:
        publish_one_cycle()
        time.sleep(1)

elif mode == "2":

    print("\nManual mode")
    print("Press Enter to publish the next message")
    print("Type q and press Enter to quit.\n")

    while True:

        command = input("> ").strip().lower()

        if command == "q":
            break

        publish_one_cycle()

else:
    print("Invalid mode selected.")