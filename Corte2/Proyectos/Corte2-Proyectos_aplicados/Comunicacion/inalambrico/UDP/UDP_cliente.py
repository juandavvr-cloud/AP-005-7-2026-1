import network
import socket
import time

SSID = "HONOR 400 Smart"
PASSWORD = "kardenaz"

# Conexión WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    time.sleep(0.5)

print("IP del cliente:", wlan.ifconfig()[0])

# Datos del servidor UDP
SERVER_IP = "10.150.83.96"
SERVER_PORT = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    mensaje = b"Dato desde ESP32 Cliente"
    sock.sendto(mensaje, (SERVER_IP, SERVER_PORT))
    print("Enviado:", mensaje)

    try:
        sock.settimeout(1)
        data, addr = sock.recvfrom(128)
        print("Respuesta:", data.decode())
    except:
        print("Sin respuesta")

    time.sleep(1)