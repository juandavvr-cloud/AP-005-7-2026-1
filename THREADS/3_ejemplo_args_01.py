import threading
import time

def saludar_usuario(nombre):
    for i in range(2):
        print(f"Hola {nombre}, haz la tarea #{i}")
        time.sleep(1)

hilo = threading.Thread(target=saludar_usuario, args=("Juan",))

hilo.start()
hilo.join()

print("Programa finalizado correctamente")