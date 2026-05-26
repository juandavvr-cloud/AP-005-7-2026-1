import threading
import time

def contador(nombre, inicio, fin, pausa):
    for i in range(inicio, fin+1):
        print(f"{nombre}: {i}")
        time.sleep(pausa)

rapido = threading.Thread(target=contador, args=("Rápido", 1, 4, 0.3))
lento = threading.Thread(target=contador, args=("Lento", 5, 8, 1.2))

rapido.start()
lento.start()

rapido.join()
lento.join()

print("Finalizó el conteo")