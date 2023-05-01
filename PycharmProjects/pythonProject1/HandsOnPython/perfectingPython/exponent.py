# Write a script called exponent.py that receives two numbers from the user
# and displays the first number raised to the power of the second number.
# A smaple run of the program should look like this(with example input

def exponent2():
    first_number = input("Enter the first number\n")
    second_number = input("Enter the second number\n")

    # if isinstance(first_number, str):
    first_no = int(first_number)
    # if isinstance(second_number, str):
    second_no = int(second_number)

    raise_to_the_power = first_no ** second_no
    print("Result is {0}".format(raise_to_the_power))


exponent2()
