import json
import time

from cnc_machine import CNCMachine

machine = CNCMachine()

while True:

    telemetry = machine.generate_telemetry()

    cycle_event = machine.generate_cycle_event()

    tool_change = machine.generate_tool_change()

    alarm = machine.generate_alarm()

    print("TELEMETRY:")
    print(json.dumps(telemetry, indent=2))

    if alarm is not None:

        print("\nALARM:")
        print(json.dumps(alarm, indent=2))

    if cycle_event is not None:

        print("\nCYCLE EVENT:")
        print(json.dumps(cycle_event, indent=2))

    if tool_change is not None:

        print("\nTOOL CHANGE:")
        print(json.dumps(tool_change, indent=2))

    print("-" * 50)

    machine.update()

    time.sleep(1)