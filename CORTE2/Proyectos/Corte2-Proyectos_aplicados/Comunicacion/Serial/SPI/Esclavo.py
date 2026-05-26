# ESP esclavo
from machine import SPI, Pin
import time

spi = SPI(1, baudrate=500000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(23), miso=Pin(19))

cs = Pin(5, Pin.IN)

buffer = bytearray(9)

def reconstruir(datos):
    matriz = [
        [datos[0], datos[1], datos[2]],
        [datos[3], datos[4], datos[5]],
        [datos[6], datos[7], datos[8]]
    ]
    return matriz

while True:
    if cs.value() == 0:  # maestro activo
        spi.readinto(buffer)
        
        matriz = reconstruir(buffer)
        print("Matriz recibida:")
        for fila in matriz:
            print(fila)
        
        time.sleep(1)