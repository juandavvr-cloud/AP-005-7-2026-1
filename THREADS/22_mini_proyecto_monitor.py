import threading
import queue
import random
import time

cola = queue.Queue()
detener = threading.Event()

def sensor():
    while not detener.is_set():
        cola.put(random.uniform(20, 30))
        time.sleep(0.5)

def mostrar():
    while not detener.is_set():
        if not cola.empty():
            print("Temperatura:", cola.get())

t1 = threading.Thread(target=sensor)
t2 = threading.Thread(target=mostrar)

t1.start()
t2.start()

time.sleep(6)
detener.set()

t1.join()
t2.join()