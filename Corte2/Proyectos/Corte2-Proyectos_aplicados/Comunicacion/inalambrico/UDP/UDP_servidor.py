import network
import socket
import time

SSID = "HONOR 400 Smart"
PASSWORD = "kardenaz"

# Conectar a WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Reinicio de interfaz (recomendado en ESP32)
wlan.active(False)
time.sleep(1)
wlan.active(True)

wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    print("Conectando...")
    time.sleep(1)

print("Servidor conectado, IP:", wlan.ifconfig()[0])

# Crear socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Puerto donde escucha
PORT = 8000
sock.bind(("0.0.0.0", PORT))

print("Servidor UDP escuchando en puerto", PORT)

while True:
    data, addr = sock.recvfrom(256)
    mensaje = data.decode().strip()
    
    print("Recibido de", addr, "->", mensaje)
    
    # Respuesta al cliente
    respuesta = "ACK desde ESP32 servidor"
    sock.sendto(respuesta.encode(), addr)