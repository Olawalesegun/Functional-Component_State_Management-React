# Py Thursday 25,05,2023
class Animal:
    def __init__(self):
        self.age = 3

    def eat(self):
        print("Eating...")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 45

    def walk(self):
        print("Swimming...")


class Fish(Animal):
    def swim(self):
        print("Swimming.....")


m = Mammal()
m.eat()
f = Fish()
print(f.age)
f.eat()
print(m.weight)
print(f.age)
