import threading
import time

class MiHilo(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        for i in range(4):
            print(self.nombre, i)
            time.sleep(1)

h1 = MiHilo("H1")
h2 = MiHilo("H2")

h1.start()
h2.start()

h1.join()
h2.join()