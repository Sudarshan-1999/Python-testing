from time import sleep
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

def thread_function(name):
    print(f"Thread {name} is Started....")
    sleep(1)
    print(f"Thread is {name} Ended.")

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(thread_function, range(7))
