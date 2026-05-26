import time

def proceso(nombre):
    print(f"Ejecutando {nombre}")
    time.sleep(1.5)
    print(f"{nombre} terminado")

inicio = time.perf_counter()

proceso("A")
proceso("B")
proceso("C")

fin = time.perf_counter()

print(f"Tiempo total: {fin - inicio:.2f} segundos")