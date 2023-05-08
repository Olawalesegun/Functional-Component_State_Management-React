from sys import getsizeof

doubles = {a: a**2 for a in range(1, 11)}
print(doubles)

double = [a ** 2 for a in range(1000000)]
doubles = (a**2 for a in range(1, 11))
print(doubles)

print(getsizeof(double))
print(getsizeof(doubles))