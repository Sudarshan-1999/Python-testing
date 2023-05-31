class Person:
    def __init__(self, name):
        self.name = name
    
    def sayName(self):
        print(f"My Name is {self.name} ")


class Engineer(Person):
    def __init__(self, name):
        super().__init__(name)
        self.profession = "Engineer"

    def sayProfession(self):
        print(self.profession)

class Doctor(Person): 
    def __init__(self, name):
        super().__init__(name)
        self.profession = "Doctor"

    def sayProfession(self):
        print(self.profession)


engineer = Engineer("Sudarshan")
engineer.sayName()
engineer.sayProfession()

doctor = Doctor("Ajay")
doctor.sayName()
doctor.sayProfession()