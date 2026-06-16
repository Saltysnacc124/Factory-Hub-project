import json
import time

from cnc_machine import CNCMachine

machine = CNCMachine()

while True:

    telemetry = machine.generate_telemetry()

    cycle_event = machine.generate_cycle_event()

    print("TELEMETRY:")
    print(json.dumps(telemetry, indent=2))

    if cycle_event is not None:

        print("\nCYCLE EVENT:")
        print(json.dumps(cycle_event, indent=2))

    print("-" * 50)

    machine.update()

    time.sleep(1)