# 1. Create a class named Employee, with a constructor ‘__init__’ method that
# accepts name and salary as parameters and set properties named name
# and salary.
# 2. Define __str__ method in Employee class so that when someone tries to
# print the object the string Name: employee_name, Salary:
# employee_salary is printed with the actual employee name and salary.
# 3. Create another class named Calculator, with methods to add, subtract,
# multiply and divide two numbers.
# 4. These methods take two numbers as parameters.
# 5. These methods will be called by a method named execute command.
# 6. Execute command takes in 3 parameters command which is string that can
# be either ‘add’, ‘sub’, ‘mul’, ‘div’, and two numbers and it will call the
# appropriate method based on command parameter.

class Calculator:
    # def __init__(self):
    #     self.num1 = num1
    #     self.num2 = num2


    def addition(self, num1, num2):
        return self.__str__(self.addition.__name__,num1 + num2)
    
    def substaction(self, num1, num2):
        return self.__str__(self.substaction.__name__,num1 - num2)
    def multipication(self, num1, num2):
        return self.__str__(self.multipication.__name__,num1 * num2) 
    def division(self, num1, num2):
        if(num2 == 0): raise Exception ("Num2 cannot be 0 ")
        else:
            return self.__str__(self.division.__name__,num1 / num2)
        
    def __str__(self, fun, result):
        print(f"The Result of {fun} {result}")
        
cal = Calculator()
cal.addition(1,2)
try:
    cal.division(3,1)
except Exception as ex:
    print(ex)
# else:
#     print("Exception Not thrown")

cal.multipication(4,5)
cal.substaction(6,7)