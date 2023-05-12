def lambdmap():
    lst = [1, 2, 3, 4, 5]
    # lst2 = (1, 2, 4, 5, 6)
   # ans1 = list(map(squarenum, lst))
   # ans = list(map(squarenum, lst2))

    print(list(filter(lambda n: n*2, lst)))
    print(list(map(lambda n: n * 2, lst)))


lambdmap()


