from threading import *
import time
def display():
    print("hi")

t1=Thread(target=display)
t1.start()
t1.setDaemon=True