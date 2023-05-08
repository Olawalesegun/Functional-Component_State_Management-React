def what_wrong_with_code():
    day, high_temperature = ('Monday', 87, 65)
    #   ANS:
    #   1.  The variable declared is more than the initialized values, Hence one variable was not initialized.
    numbers = [1, 2, 3, 4, 5]
    numbers[10]
    #   ANS:
    #   2. It won't run because the variable index 10 cannot be accessed because it is out of range of elements in the numbers List.
    name = 'amanda'
    name[0] = 'A'
    #   ANS:
    #   3. Not run --- Strings are immutable, hence you can not chnage or alter it state, rather you can assign to other variables.
    numbers = [1, 2, 3, 4, 5]
    numbers[3.4]
    #   ANS
    #   4:The indices for q list must be integeres or slices, and not a tuple.
    student_tuple = ('Amanda', 'Blue', [98, 75, 87])
    student_tuple[0] = 'Ariana'
    #   ANS:
    #   5.. You can not reassign to a Tuple.
    ('Monday', 87, 65) + 'Tuesday'
    #   ANS
    #   6. This will not effect as it will throw a syntax erroe.
    'A' += ('B', 'C')
    #   ANS:
    #   THis will not run
    x = 7
    del x =
    print(x)
    #   ANS:
    #   This will throw a syntax error.
    numbers = [1, 2, 3, 4, 5]
    numbers.index(10)
    #   ANS:
    #   This will ws throw an error ad 10 is not identified    j)
    numbers = [1, 2, 3, 4, 5]
    numbers.extend(6, 7, 8)
    #   ANS:
    # It won't run, list of index is out of range.
    numbers = [1, 2, 3, 4, 5]
    numbers.remove(10)
    #   ANS:
    #   You can't remove what doesn't exists.
    values = []
    values.pop()
    #   ANS:
    #   THis is an inbuilt method.