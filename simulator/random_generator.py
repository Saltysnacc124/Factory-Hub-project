import random
import json
import time
from datetime import datetime, timezone

def generate_telemetry():
    payload = {
        "message_type": "telemetry",
        "machine_id": "CNC_001",
        "timestamp": datetime.now(timezone.utc).isoformat(),

        "status": "RUNNING",
        "state": "AUTO",

        "program_id": "P1001",
        "tool_id": random.randint(1, 12),

        "cycle_active": True,
        "part_count": random.randint(100, 500),

        "spindle_rpm": round(random.uniform(7000, 9000), 2),
        "feed_rate": round(random.uniform(1000, 2000), 2),

        "axis_position": {
            "x": round(random.uniform(0, 500), 3),
            "y": round(random.uniform(0, 500), 3),
            "z": round(random.uniform(-100, 0), 3)
        },

        "load": {
            "spindle": round(random.uniform(20, 70), 2),
            "x_axis": round(random.uniform(10, 50), 2),
            "y_axis": round(random.uniform(10, 50), 2),
            "z_axis": round(random.uniform(10, 50), 2)
        },

        "temperature": {
            "spindle": round(random.uniform(35, 55), 2),
            "motor": round(random.uniform(30, 50), 2)
        },

        "override": {
            "feed_override": 100,
            "spindle_override": 100
        }
    }

    return payload




while True:
    payload = generate_telemetry()

    print(json.dumps(payload, indent=2))
    print("-" * 50)

    time.sleep(5)