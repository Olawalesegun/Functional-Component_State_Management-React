def swap():
    a = 1
    b = 2
    print(a, b)
    c = a
    a = b
    b = c
    print(c, a)

    # Second method
    a = 1
    b = 2
    a, b = b, a
    print(a, b)


swap()