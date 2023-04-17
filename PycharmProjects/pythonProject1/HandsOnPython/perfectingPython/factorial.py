def factorial(number):
    increasedno = number + 1
    numberconvertedtototal = 1
    for i in range(1, increasedno):
        numberconvertedtototal = numberconvertedtototal * i
    print(numberconvertedtototal)

if __name__ == "__main__":
    factorial(5)