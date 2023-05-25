# Py Thursday 25,05,2023
class Text(str):

    def duplicate(self):
        return self + self


t1 = Text("shola")
t1.duplicate()