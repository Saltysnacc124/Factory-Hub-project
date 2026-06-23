import json
import paho.mqtt.client as mqtt

from handlers import (
    handle_telemetry,
    handle_alarm,
    handle_tool_change,
    handle_cycle_event
)

BROKER = "localhost"
PORT = 1883

TOPIC = "cnc/CNC_001/#"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected Successfully")

        client.subscribe(TOPIC)
        print(f"Subscribed to {TOPIC}")

    else:
        print(f"Connection failed with code {rc}")


def on_message(client, userdata, msg):

    topic = msg.topic

    payload = msg.payload.decode()

    data = json.loads(payload)

    message_type = topic.split("/")[-1]

    if message_type == "telemetry":
        handle_telemetry(data)

    elif message_type == "alarm":
        handle_alarm(data)

    elif message_type == "cycle_event":
        handle_cycle_event(data)

    elif message_type == "tool_change":
        handle_tool_change(data)

    else:
        print(f"Unknown message type: {message_type}")


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)

client.loop_forever()