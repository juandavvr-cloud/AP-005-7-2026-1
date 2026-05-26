import threading
import time

detener = threading.Event()

def tarea():
    while not detener.is_set():
        print("Revisión periódica...")
        time.sleep(1)

h = threading.Thread(target=tarea)
h.start()

time.sleep(5)
detener.set()

h.join()