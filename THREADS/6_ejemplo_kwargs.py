import threading
import time

def proceso(nombre, veces, pausa):
    for i in range(veces):
        print(f"{nombre} ejecución {i}")
        time.sleep(pausa)

hilo = threading.Thread(
    target=proceso,
    kwargs={"nombre": "Proceso kwargs", "veces": 3, "pausa": 0.6}
)

hilo.start()
hilo.join()

print("Fin del proceso")