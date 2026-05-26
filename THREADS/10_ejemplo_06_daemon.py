import threading
import time

def fondo():
    while True:
        print("Ejecutándose en segundo plano...")
        time.sleep(1)

h = threading.Thread(target=fondo, daemon=True)
h.start()

for i in range(4):
    print(f"Principal {i}")
    time.sleep(1)

print("Programa terminado")