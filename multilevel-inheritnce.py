class A: 
    def PrintA(self):
        print("From A")
class B:
    def PrintB(self):
        print("From B")
class C(A, B):
    def PrintC(self):
        print("From C")
obj = C()

obj.PrintA()
obj.PrintB()
obj.PrintC()
