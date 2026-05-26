import threading
import time

detener = threading.Event()

def trabajo():
    while not detener.is_set():
        print("Procesando...")
        time.sleep(1)

h = threading.Thread(target=trabajo)
h.start()

while True:
    comando = input("Escribe comando: ")
    if comando == "salir":
        detener.set()
        break

h.join()