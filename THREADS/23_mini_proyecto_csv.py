import threading
import queue
import time
import random
import csv

cola = queue.Queue()
detener = threading.Event()

def generar():
    while not detener.is_set():
        cola.put(random.randint(1,100))
        time.sleep(0.3)

def guardar():
    with open("registro.csv","w",newline="") as f:
        writer = csv.writer(f)
        while not detener.is_set():
            if not cola.empty():
                writer.writerow([cola.get()])

t1 = threading.Thread(target=generar)
t2 = threading.Thread(target=guardar)

t1.start()
t2.start()

time.sleep(5)
detener.set()

t1.join()
t2.join()