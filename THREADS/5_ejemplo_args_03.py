import threading
import time

def sensor(nombre, unidad, minimo, maximo):
    for _ in range(4):
        valor = (minimo + maximo) / 2
        print(f"{nombre}: {valor} {unidad}")
        time.sleep(1)

temp = threading.Thread(target=sensor, args=("Temperatura", "°C", 18, 28))
dist = threading.Thread(target=sensor, args=("Distancia", "cm", 10, 60))

temp.start()
dist.start()

temp.join()
dist.join()

print("Sensores finalizados")