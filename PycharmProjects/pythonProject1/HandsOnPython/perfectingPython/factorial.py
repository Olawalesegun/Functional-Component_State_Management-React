def factorial(number):
    increased_no = number + 1
    number_converted_to_total = 1
    for i in range(1, increased_no):
        number_converted_to_total = number_converted_to_total * i
    print(number_converted_to_total)


if __name__ == "__main__":
    factorial(5)
