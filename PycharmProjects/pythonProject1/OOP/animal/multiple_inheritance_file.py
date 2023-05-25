# Py Thursday 25,05,2023
class Person:
    def greet(self):
        print("Person greeting")


class Employee:

    def greet(self):
        print("Employee greeting")


class Admin(Person, Employee):
    pass


admin1 = Admin()
admin1.greet()
