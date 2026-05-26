from machine import Pin, I2C, UART
import time

# I2C (maestro)
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
SLAVE_ADDR = 0x08

# UART para recibir del Arduino
uart = UART(1, baudrate=115200, tx=17, rx=16)

while True:
    mensaje = "Hola Arduino\n"
    
    # Enviar por I2C
    try:
        i2c.writeto(SLAVE_ADDR, mensaje.encode())
        print("ESP32 envió:", mensaje)
    except Exception as e:
        print("Error I2C:", e)
    
    # Leer lo que Arduino devuelve por UART
    if uart.any():
        data = uart.read()
        print("Desde Arduino:", data.decode(), end='')
    
    time.sleep(1)