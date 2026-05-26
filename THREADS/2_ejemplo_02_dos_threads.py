import threading
import time

def mostrar(nombre):
    for i in range(6):
        print(f"{nombre} -> {i}")
        time.sleep(0.8)

h1 = threading.Thread(target=mostrar, args=("Proceso A",))
h2 = threading.Thread(target=mostrar, args=("Proceso B",))

h1.start()
h2.start()