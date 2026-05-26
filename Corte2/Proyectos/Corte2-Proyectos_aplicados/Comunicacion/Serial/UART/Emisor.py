# Codigo Emisor
from machine import UART
import time

uart = UART(2, baudrate=115200, rx=16, tx=17)

print("ESP1 iniciando...")
time.sleep(3)
uart.read()

buffer = b""
conectado = False
t0 = time.ticks_ms()

while True:
    # enviar READY si no está conectado
    if not conectado and time.ticks_diff(time.ticks_ms(), t0) > 1000:
        t0 = time.ticks_ms()
        uart.write("READY\n")
        print("Enviando READY")

    # enviar datos si ya conectó
    if conectado and time.ticks_diff(time.ticks_ms(), t0) > 1000:
        t0 = time.ticks_ms()
        uart.write("Hola desde ESP1\n")

    # recibir datos
    if uart.any():
        data = uart.read()
        if data:
            buffer += data

            while b'\n' in buffer:
                line, buffer = buffer.split(b'\n', 1)
                msg = line.decode().strip()
                print("Recibido:", msg)

                if msg == "OK":
                    conectado = True
                    print("Conectado")

                elif msg == "READY":
                    uart.write("OK\n")
                    conectado = True