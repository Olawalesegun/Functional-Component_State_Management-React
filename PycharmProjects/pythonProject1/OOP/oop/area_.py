from math import pi


def area_of_c(r):
    if r < 0:
        raise ValueError("Radius cannot be negative")
    if r == "g":
        raise TypeError("Kindly input an int type")
    return pi * (r ** 2)


def multiply(x, y):
    try:
        return x * y
    except TypeError:
        return f"Kindly input an int type"
    except ValueError:
        return f"Kindly input a non negative Value"