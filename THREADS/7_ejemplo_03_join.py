import threading
import time

def tarea(nombre, tiempo):
    print(f"Iniciando {nombre}")
    time.sleep(tiempo)
    print(f"Finalizó {nombre}")

t1 = threading.Thread(target=tarea, args=("Proceso 1", 2))
t2 = threading.Thread(target=tarea, args=("Proceso 2", 3))

t1.start()
t2.start()

t1.join()
t2.join()

print("Todos los procesos terminaron")