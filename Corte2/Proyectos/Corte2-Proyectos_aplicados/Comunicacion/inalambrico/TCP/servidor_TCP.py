import network
import socket
import time

SSID = "HONOR 400 Smart"
PASSWORD = "kardenaz"

# Conectar WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.active(False)
time.sleep(1)
wlan.active(True)

wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    print("Conectando...")
    time.sleep(1)

print("Servidor conectado, IP:", wlan.ifconfig()[0])

# Crear socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 8000
sock.bind(("0.0.0.0", PORT))
sock.listen(1)  # Espera clientes

print("Servidor TCP escuchando en puerto", PORT)

while True:
    conn, addr = sock.accept()
    print("Cliente conectado desde:", addr)

    try:
        while True:
            data = conn.recv(256)
            if not data:
                break

            mensaje = data.decode().strip()
            print("Recibido ->", mensaje)

            respuesta = "ACK desde ESP32 servidor TCP"
            conn.send(respuesta.encode())

    except:
        print("Error con cliente")

    conn.close()
    print("Cliente desconectado")