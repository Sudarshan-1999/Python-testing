# in python most od the thread related task are perform using the threading module

from time import sleep
from threading import Thread

def thread_function(name):
    print(f"Thread {name} is started")
    sleep(2)
    print(f"Thread is {name} ended.")

print("Main - Started")
t = Thread(target=thread_function, args=("New",))

print("Main - Before Starting Thread")
t.start()
print("Main - Waiting for thread to finish")
print("Main - Before Starting Thread")
print("Main - Done")
