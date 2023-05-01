def multiplication_table(num):
    for count in range(1, 13):
        numa = num * count
        print(f"{num} * {count} = {numa}")


num = int(input("Enter a number: "))
multiplication_table(num)


def multiplication2_table():
    for count in range(1, 13):
        for count2 in range(1, 13):
            print(f"{count} x {count2} = {count * count2} \n")
        print(f"=============================")


multiplication2_table()
