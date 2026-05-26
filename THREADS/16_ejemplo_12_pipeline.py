import threading
import queue
import time
import random

cola = queue.Queue()
detener = threading.Event()

def generar():
    while not detener.is_set():
        valor = random.randint(1,10)
        cola.put(valor)
        time.sleep(0.3)

def procesar():
    while not detener.is_set():
        if not cola.empty():
            dato = cola.get()
            print("Dato procesado:", dato*3)

t1 = threading.Thread(target=generar)
t2 = threading.Thread(target=procesar)

t1.start()
t2.start()

time.sleep(4)
detener.set()

t1.join()
t2.join()