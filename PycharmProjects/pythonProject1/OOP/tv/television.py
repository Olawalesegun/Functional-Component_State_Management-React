class Television:

    def __init__(self, name: str):
        self.name = name
        self.status = False
        self.volume = 0
        self.channel = 1

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.__name = name

    def isOn(self):
        status = not self.status

    def isOff(self):
        status = False

    def increase_volume(self):
        if self.volume > 0 and self.volume > 100:
            volume = self.volume + 1

    def decrease_volume(self):
        if self.volume > 0:
            volume = self.volume - 1

    def __str__(self):
        return f"{self.name} {self.increase_volume()}"


tv = Television("Panasonic")
# tv.isOn() = True
print(tv)
print(tv.increase_volume())
