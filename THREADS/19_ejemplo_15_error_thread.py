import threading
import time

def error():
    time.sleep(1)
    print(5/0)

h = threading.Thread(target=error)
h.start()

h.join()