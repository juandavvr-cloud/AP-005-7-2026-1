import threading
import time

def proceso(nombre):
    print(f"Inicia {nombre}")
    time.sleep(1.5)
    print(f"Fin {nombre}")

inicio = time.perf_counter()

hilos = []

for i in range(3):
    h = threading.Thread(target=proceso, args=(f"Hilo {i+1}",))
    hilos.append(h)
    h.start()

for h in hilos:
    h.join()

fin = time.perf_counter()

print(f"Tiempo total con threads: {fin - inicio:.2f}")