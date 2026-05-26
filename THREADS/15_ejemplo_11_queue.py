import threading
import queue
import random
import time

cola = queue.Queue()

def prod():
    for _ in range(8):
        dato = random.randint(1,50)
        cola.put(dato)
        print("Produce:", dato)
        time.sleep(0.4)

def cons():
    for _ in range(8):
        dato = cola.get()
        print("Consume:", dato)

t1 = threading.Thread(target=prod)
t2 = threading.Thread(target=cons)

t1.start()
t2.start()

t1.join()
t2.join()