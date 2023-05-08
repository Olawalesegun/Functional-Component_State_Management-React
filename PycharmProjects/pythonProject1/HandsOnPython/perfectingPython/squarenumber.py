def squarenum(num):
    for i in range(1, 2):
        num *= num
    print(num)
    return num

    # or
    # num ** 2


squarenum(2)

    # a map takes a function and an iterable..
    # what you are to do is pass a function into the map and also an array which is iterable

lst = [1, 2, 3, 4, 5]
lst2 = (1, 2, 4, 5,6)
ans1 = list(map(squarenum, lst))
ans = list(map(squarenum, lst2))
#print(ans)
#print(ans1)
# in the map
