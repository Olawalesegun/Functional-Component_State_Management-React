class Human:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello {self.name}")

    def walk(self):
        print(f"{self.name} is working")

    @classmethod
    def blue_eyes(cls):
        pass

    def __str__(self):
        return f"{self.name}"


human1 = Human("esther")
human2 = Human("Torin")
print(human1.greet())
print(human2.greet())
print(human1.name)
print(human1.walk())

# esther = Human()
# print(esther.greet())
