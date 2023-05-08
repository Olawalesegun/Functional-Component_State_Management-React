


def odd_numb(num):
    # Declare a list, 1 to typing_extensionsdeclare a function to give us odd numbers
    # new_num = len(num)
    # for i in range(new_num):
    if num % 2 == 1:
        print(num)
    return num


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numb(9)

def odd_num(numb):
    odd = []
    for i in numb:
        if i % 2 != 0:
            odd.append(i)
    return odd

def odd_value(n):
    if n % 2 != 0:
        return n

#when you need to get the element, and affect it directly.. you don't need to determine the length'
print(odd_num(lst))
print(list(filter(odd_value, lst)))

