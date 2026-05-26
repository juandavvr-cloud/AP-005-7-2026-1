import network
import time
from umqtt.simple import MQTTClient

SSID = "HONOR 400 Smart"
PASSWORD = "kardenaz"

BROKER = "broker.hivemq.com"
PORT = 1883

TOPIC_PUB = b"juan/robot/telemetria"
TOPIC_SUB = b"juan/robot/estado"

def callback(topic, msg):
    print("Recibido:", topic, msg)

# WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    time.sleep(0.5)

print("ESP1 IP:", wlan.ifconfig()[0])

# MQTT
client = MQTTClient("esp32_pub", BROKER, port=PORT)
client.set_callback(callback)
client.connect()
client.subscribe(TOPIC_SUB)

print("ESP1 conectado a MQTT")

while True:
    mensaje = "Hola desde ESP32 #1"
    client.publish(TOPIC_PUB, mensaje)
    print("Enviado:", mensaje)

    client.check_msg()
    time.sleep(2)