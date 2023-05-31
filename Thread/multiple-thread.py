from time import sleep
from threading import Thread
def thread_function(name):
    print(f"Thread {name} is Started....")
    sleep(2)
    print(f"Thread is {name} Ended.")

threads =[]
for i in range(5):
    print(f"Main - Creating and Starting thread {i}")
    t = Thread(target=thread_function, args=(i,))
    threads.append(t)
    t.start()
for i, x in enumerate(threads):
    print(f"Main - Before Joining thread {i}")
    x.join()
    print(f"Main - After Joininig thread {i}")

