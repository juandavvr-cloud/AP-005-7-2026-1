import threading
import time

def error_controlado():
    try:
        time.sleep(1)
        print(5/0)
    except:
        print("Error detectado en thread")

h = threading.Thread(target=error_controlado)
h.start()

h.join()