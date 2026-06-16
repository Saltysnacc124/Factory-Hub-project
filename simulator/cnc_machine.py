import random
from datetime import datetime, timezone



class CNCMachine:
    
    def __init__(self):
        
        self.machine_id = "CNC_001"
        
        self.status = "IDLE"
        self.state = "AUTO"
        
        self.program_id = "P1001"

        self.tool_id = 1

        self.part_count = 0

        self.cycle_active = False

        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

        self.spindle_rpm = 0.0
        self.feed_rate = 0.0

        self.spindle_load = 0.0

        self.x_axis_load = 0.0
        self.y_axis_load = 0.0
        self.z_axis_load = 0.0

        self.spindle_temp = 25.0
        self.motor_temp = 25.0

        self.cycle_time = 30
        self.current_cycle_time = 0

        self.current_cycle_id = 1

        self.last_cycle_event = None
        self.last_tool_change = None
        self.last_alarm = None

    
    def update(self):

    # Start a cycle if idle
        if self.status == "IDLE":
            
            self.status = "RUNNING"
            self.cycle_active = True
            self.current_cycle_time = 0

            self.last_cycle_event = "CYCLE_STARTED"

    # Behavior while running
        if self.status == "RUNNING":

            self.current_cycle_time += 1

            self.spindle_rpm = 8000
            self.feed_rate = 1500

            self.x += random.uniform(-0.5, 0.5)
            self.y += random.uniform(-0.5, 0.5)
            self.z += random.uniform(-0.1, 0.1)

            self.spindle_load = random.uniform(40, 70)

            self.x_axis_load = random.uniform(20, 50)
            self.y_axis_load = random.uniform(20, 50)
            self.z_axis_load = random.uniform(10, 40)

            self.spindle_temp += 0.1
            self.motor_temp += 0.05

            if self.current_cycle_time >= self.cycle_time:
                
                self.part_count += 1
                self.status = "IDLE"
                self.cycle_active = False

                self.last_cycle_event = "CYCLE_COMPLETED"
                self.current_cycle_id += 1

    # Cooling when idle
        if self.status == "IDLE":

            self.spindle_rpm = 0
            self.feed_rate = 0

            self.spindle_load = 0
            self.x_axis_load = 0
            self.y_axis_load = 0
            self.z_axis_load = 0

            self.spindle_temp = max(25, self.spindle_temp - 0.05)
            self.motor_temp = max(25, self.motor_temp - 0.03)


    def generate_telemetry(self):

        return {
        "message_type": "telemetry",
        "machine_id": self.machine_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),

        "status": self.status,
        "state": self.state,

        "program_id": self.program_id,
        "tool_id": self.tool_id,

        "cycle_active": self.cycle_active,
        "part_count": self.part_count,

        "spindle_rpm": self.spindle_rpm,
        "feed_rate": self.feed_rate,

        "axis_position": {
            "x": self.x,
            "y": self.y,
            "z": self.z
        },

        "load": {
            "spindle": self.spindle_load,
            "x_axis": self.x_axis_load,
            "y_axis": self.y_axis_load,
            "z_axis": self.z_axis_load
        },

        "temperature": {
            "spindle": self.spindle_temp,
            "motor": self.motor_temp
        },

        "override": {
            "feed_override": 100,
            "spindle_override": 100
        }
    }


    def generate_cycle_event(self):

        if self.last_cycle_event is None:
            return None

        payload = {

            "message_type": "cycle_event",

            "machine_id": self.machine_id,

            "timestamp": datetime.now(timezone.utc).isoformat(),

            "event": self.last_cycle_event,

            "cycle_id": f"C{self.current_cycle_id:05d}",

            "program_id": self.program_id,

            "tool_id": self.tool_id,

            "cycle_time_sec": self.current_cycle_time,

            "part_number": self.part_count
        }

        self.last_cycle_event = None

        return payload