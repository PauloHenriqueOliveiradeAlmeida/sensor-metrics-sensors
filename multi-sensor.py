import random
import time
import paho.mqtt.client as mqtt_client
import json

broker = "localhost"
port = 1883
topic = "update-sensor-metrics"


def simulate_sensors():
    while True:
        temperature = random.uniform(10.0, 500.0)
        humidity = 510 - (temperature / 2)

        client.publish(
            topic, json.dumps({"sensor_name": "temperature", "value": temperature})
        )
        client.publish(
            topic, json.dumps({"sensor_name": "humidity", "value": humidity})
        )

        time.sleep(1)


client = mqtt_client.Client()
client.connect(broker, port, 60)

simulate_sensors()
