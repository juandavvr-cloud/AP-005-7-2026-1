import network
import time
from umqtt.simple import MQTTClient

SSID = "HONOR 400 Smart"
PASSWORD = "kardenaz"

BROKER = "broker.hivemq.com"
PORT = 1883

TOPIC_SUB = b"juan/robot/telemetria"
TOPIC_PUB = b"juan/robot/estado"

def callback(topic, msg):
    print("Recibido:", topic, msg)

    # Respuesta automática
    client.publish(TOPIC_PUB, b"ACK desde ESP32 #2")

# WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    time.sleep(0.5)

print("ESP2 IP:", wlan.ifconfig()[0])

# MQTT
client = MQTTClient("esp32_sub", BROKER, port=PORT)
client.set_callback(callback)
client.connect()
client.subscribe(TOPIC_SUB)

print("ESP2 conectado a MQTT")

while True:
    client.check_msg()
    time.sleep(0.1)