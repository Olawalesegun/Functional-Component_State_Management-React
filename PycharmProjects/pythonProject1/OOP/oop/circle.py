import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    # @property
    # def area_of_radius(self):
    #     return self.radius()
    #
    # @area_of_radius.setter
    # def area_of_radius(self, value):
    #     if value < 0:
    #         ValueError("radius cannot be less than 0")
    #     self.__ = area
    #
    # def perimeter_of_circle(self):
    #     area = math.pi * self.radius ** 2
             ##
    def areas_of_radius(self):
        area = math.pi * self.radius ** 2
        return f"The areas of radius is {area}"

    def perimeter_of_circle(self):
        pi = 2 * math.pi * self.radius
        return f"the area of a radius is {pi}"


circle1 = Circle(18)
print(circle1.perimeter_of_circle())

#self.radius = math.sqrt(value / math.pi)
