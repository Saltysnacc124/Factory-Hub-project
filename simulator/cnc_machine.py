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
        self.last_completed_cycle_id = None

        self.last_cycle_event = None
        self.last_tool_change = None
        self.last_alarm = None

        self.tool_offset = 0.0
        self.tool_wear = 0.0
        self.tool_change_interval = 2   #Actual=10; Test=2

        self.previous_tool_id = None
        self.last_tool_change = None

        self.feed_override = 100
        self.spindle_override = 100

        self.alarm_active = False

        self.alarm_code = None
        self.alarm_message = None
        self.alarm_severity = None

    
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

            self.tool_wear += 0.01

            if self.current_cycle_time >= self.cycle_time:
                
                self.part_count += 1
                self.status = "IDLE"
                self.cycle_active = False

                self.last_cycle_event = "CYCLE_COMPLETED"
                self.last_completed_cycle_id = self.current_cycle_id
                self.current_cycle_id += 1

            #Tool Change
                if self.part_count % self.tool_change_interval == 0:

                    self.previous_tool_id = self.tool_id
                    
                    self.tool_id += 1

                    self.last_tool_change = {
                        "previous_tool_id": self.previous_tool_id,
                        "new_tool_id": self.tool_id
                    }

                    self.tool_offset = round(random.uniform(-0.02, 0.02), 3)
                    self.tool_wear = 0

        #Alarm - Spindle Temp High (actual threshold=80, testing=40)
            if self.spindle_temp > 40 and not self.alarm_active:

                self.alarm_active = True

                self.alarm_code = "TEMP_HIGH"

                self.alarm_message = "Spindle temperature exceeded threshold"

                self.alarm_severity = "HIGH"

                self.last_alarm = {
                    "alarm_code": self.alarm_code,
                    "message": self.alarm_message,
                    "severity": self.alarm_severity
                }

                self.status = "ALARM"

                self.cycle_active = False

    # Cooling when idle/alarm
        if self.status != "RUNNING":

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
        "cycle_id": f"C{self.current_cycle_id:05d}",

        "cycle_active": self.cycle_active,
        "current_cycle_time": self.current_cycle_time,
        "cycle_time_target": self.cycle_time,
        "part_count": self.part_count,

        "spindle_rpm": round(self.spindle_rpm, 2),
        "feed_rate": round(self.feed_rate, 2),

        "axis_position": {
            "x": round(self.x, 2),
            "y": round(self.y, 2),
            "z": round(self.z, 2)
        },

        "load": {
            "spindle": round(self.spindle_load, 2),
            "x_axis": round(self.x_axis_load, 2),
            "y_axis": round(self.y_axis_load, 2),
            "z_axis": round(self.z_axis_load, 2)
        },

        "temperature": {
            "spindle": round(self.spindle_temp, 2),
            "motor": round(self.motor_temp, 2)
        },

        "tool_wear": round(self.tool_wear, 2),

        "override": {
            "feed_override": self.feed_override,
            "spindle_override": self.spindle_override
        }
    }


    def generate_cycle_event(self):

        if self.last_cycle_event is None:
            return None

        if self.last_cycle_event == "CYCLE_COMPLETED":
            cycle_id = f"C{self.last_completed_cycle_id:05d}"
        else:
            cycle_id = f"C{self.current_cycle_id:05d}"

        payload = {

            "message_type": "cycle_event",

            "machine_id": self.machine_id,

            "timestamp": datetime.now(timezone.utc).isoformat(),

            "event": self.last_cycle_event,

            "cycle_id": cycle_id,

            "program_id": self.program_id,

            "tool_id": self.tool_id,

            "cycle_time_sec": self.current_cycle_time,

            "part_number": self.part_count
        }

        self.last_cycle_event = None

        return payload

    
    def generate_tool_change(self):

        if self.last_tool_change is None:
            return None
            
        payload = {
            "message_type": "tool_change",

            "machine_id": self.machine_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),

            "tool_id": self.tool_id,
            "previous_tool_id": self.previous_tool_id,

            "tool_offset": self.tool_offset,
            "tool_wear": round(self.tool_wear, 2),

            "reason": "TOOL_LIFE_EXPIRED"
        }

        self.last_tool_change = None

        return payload

    
    def generate_alarm(self):

        if self.last_alarm is None:
            return None

        payload = {
            "message_type": "alarm",

            "machine_id": self.machine_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),

            "alarm_code": self.alarm_code,
            "message": self.alarm_message,
            "severity": self.alarm_severity,

            "status": self.status,
            "active": self.alarm_active
        }

        self.last_alarm = None

        return payload