# Codigo Receptor
from machine import UART
import time

uart = UART(2, baudrate=115200, rx=16, tx=17)

print("ESP32 receptor listo")

buffer = b""

while True:
    if uart.any():
        data = uart.read()
        if data:
            buffer += data

            while b'\n' in buffer:
                line, buffer = buffer.split(b'\n', 1)
                msg = line.decode().strip()
                print("Emisor dice:", msg)

                # Responder
                uart.write("Recibido por ESP32\n")

    time.sleep(0.01)
