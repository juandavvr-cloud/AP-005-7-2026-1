import threading

contador = 0
lock = threading.Lock()

def sumar():
    global contador
    for _ in range(80000):
        with lock:
            contador += 1

h1 = threading.Thread(target=sumar)
h2 = threading.Thread(target=sumar)

h1.start()
h2.start()

h1.join()
h2.join()

print("Resultado protegido:", contador)