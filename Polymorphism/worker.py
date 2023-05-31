class Worker:
    def work(self):
        print("Working")

    def performTask(self):
        print("Performing Task : ", end='')
        self.work()

class DeliveryMan(Worker):
    def work(self):
        print("Delivering Goods")

class LumberJack(Worker):
    def work(self):
        print("Cutting Woods")


deliveryMan = DeliveryMan()
lumberJack = LumberJack()

deliveryMan.performTask()
lumberJack.performTask()