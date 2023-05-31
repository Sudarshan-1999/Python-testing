from time import sleep
from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor

class Counter:
    def __init__(self):
        self.value = 0
        self.__lock = Lock()

    def update(self, name):
        print("Update Started on Thread " + str(name))
        with self.__lock:
            print("Lock Aquired by " + str(name))
            val = self.value
            val +=1
            sleep(1)
            self.value = val
        print("Lock Release by " + str(name))
    
count = Counter()

with ThreadPoolExecutor(max_workers=3) as executor:
    for index in range(3):
        executor.submit(count.update, index)
        
print(count.value)
print("Done")

