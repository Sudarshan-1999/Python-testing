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

class Employee:
    def __init__(self, salary):
        # self.name = name
        self.salary = int(salary)

    def employee_name(self, name):
        # self.__str__ = name
        # print(f"The Employee name is {self.__str__}")
        self.__str__(name)

    def __str__(self, name):
        self.name = name
        print(f"The Object called from employee : {self.name}")

    def Salary(self):
        print(f"Employee Salary is {self.salary}")

emp1 = Employee(15000)
emp1.employee_name("Ajay")

emp1.Salary()

emp2 = Employee(20000)
emp2.employee_name("Vijay")
emp2.Salary()


