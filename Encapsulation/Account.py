class Account:
    def __init__(self):
        self.setBalance(10) 

    def setBalance(self, balance):
        self.__balance = balance
    
    def getBalance(self):
        print(self.__balance)
        

acc = Account()
acc.getBalance()
acc.setBalance(500)
acc.getBalance()