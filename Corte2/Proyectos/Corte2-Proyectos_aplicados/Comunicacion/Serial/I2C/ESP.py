from machine import Pin, I2C
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=50000)
addr = 0x08

saludo = "Hola Arduino"

print("ESP32 lista")

while True:
    try:
        print("ESP:",saludo)
        i2c.writeto(addr, saludo.encode())
        time.sleep(1)

        raw = i2c.readfrom(addr, 32)

        limpio = raw.split(b'\x00')[0]
        limpio = limpio.replace(b'\xff', b'')

        print("Arduino responde:", limpio.decode('utf-8', 'ignore'))

    except Exception as e:
        print("Error:", repr(e))

    time.sleep(3)