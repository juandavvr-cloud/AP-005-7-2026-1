import threading
import time

evento = threading.Event()

def tarea():
    while not evento.is_set():
        print("Trabajando...")
        time.sleep(1)

h = threading.Thread(target=tarea)
h.start()

time.sleep(4)
evento.set()

h.join()
print("Thread detenido")