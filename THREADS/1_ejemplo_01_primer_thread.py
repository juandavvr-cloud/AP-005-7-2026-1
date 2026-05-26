import threading
import time

def tarea_secundaria():
    for i in range(4):
        print(f"[SECUNDARIO] Iteración {i}")
        time.sleep(5.0)

hilo = threading.Thread(target=tarea_secundaria)

hilo.start()

print("[PRINCIPAL] Inicio del programa")