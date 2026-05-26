import network
import socket
import time

SSID = "HONOR 400 Smart"
PASSWORD = "kardenaz"

# Conectar WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    time.sleep(0.5)

print("Cliente conectado, IP:", wlan.ifconfig()[0])

# IP del servidor
SERVER_IP = "10.150.83.96"
SERVER_PORT = 8000

# Crear socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Conectando al servidor...")
sock.connect((SERVER_IP, SERVER_PORT))
print("Conectado al servidor")

while True:
    mensaje = "Hola desde cliente TCP"
    sock.send(mensaje.encode())
    print("Enviado:", mensaje)

    try:
        data = sock.recv(128)
        print("Respuesta:", data.decode())
    except:
        print("Error recibiendo")

    time.sleep(2)