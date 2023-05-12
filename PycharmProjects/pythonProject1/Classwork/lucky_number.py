import random


def lucky_num():
    # Enter a lucky number  and when luck number is equal to the number set it should say congratulations
    number = 0
    rand = random.randrange(1, 8)
    while number != rand:
        number = input("Enter a number to determine the lucky number, from 1 to 8: ")
        if number == rand:
            print("Congratulations, you have entered the lucky number")


lucky_num()