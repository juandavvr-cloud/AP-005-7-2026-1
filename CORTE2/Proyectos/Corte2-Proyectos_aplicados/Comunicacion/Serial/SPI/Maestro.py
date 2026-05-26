# ESP Maestro
from machine import SPI, Pin
import time
import struct

spi = SPI(1, baudrate=500000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(23), miso=Pin(19))

cs = Pin(5, Pin.OUT)
cs.value(1)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Aplanar matriz
data = []
for fila in matriz:
    for val in fila:
        data.append(val)

while True:
    cs.value(0)  # activar esclavo
    
    # enviar como bytes
    spi.write(bytearray(data))
    
    cs.value(1)  # desactivar
    
    print("Matriz enviada:", matriz)
    time.sleep(2)