import random
import time
import paho.mqtt.client as mqtt_client
import json

broker = "localhost"
port = 1883
topic = "update-sensor-metrics"


def simulate_sensor():
    while True:
        humidity = random.uniform(10.0, 200.0)
        client.publish(
            topic, json.dumps({"sensor_name": "humidity", "value": humidity})
        )
        time.sleep(1)


client = mqtt_client.Client()
client.connect(broker, port, 60)

simulate_sensor()
