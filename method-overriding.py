class Base:
    def add(self, a, b):
        return a + b

class Derived(Base):
    def add(self, a, b):
        return a + b + 1
    
base = Base()
derived = Derived()

print(base.add(1,2))
print(derived.add(1,3))
