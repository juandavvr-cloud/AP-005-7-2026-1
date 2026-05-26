import threading
import time
import random

def sensor():
    while True:
        temp = random.uniform(19, 31)
        print(f"Temp: {temp:.2f}")
        time.sleep(0.7)

h = threading.Thread(target=sensor, daemon=True)
h.start()

for i in range(8):
    print("Sistema activo", i)
    time.sleep(0.5)