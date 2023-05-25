# Py Thursday 25,05,2023
import statistics
from collections import Counter


def repeated_func(*args):
    print(statistics.mode(args))
    print(statistics.mode)
    return statistics.mode(args)


# Another approach using the counter method
# In here we had to import the collection package to use the counter


def repeated_func1(*args):
    count = Counter(args)
    print(count.most_common(1))
    return count.most_common(2)
    # highest_no = Counter.most_common(args)
    # print(highest_no)
    # return highest_no


## THIRD APPROACH USING NON INBUILT METHOD
# def repeated_fun2(*args2):
#     new_set = set(args2)
#     count = 0
#     length_of_args = len(new_set)
#     # for items in range(length_of_args):
#     #     if new_set[count]
#     # count = 0

# for items in args2:

# for items2 in args:
#     if items == items2:
#         new_account[count] = count + 1
# if items == args[count]:
#     count + 1

# write a func that findsnthe most repeated item in a list and returns the item.]
# if count
# if items > 1:
#     new_count[count] = items
#     count + 1
# print(new_count)

# if items == items:
#     new_count = items
# for n_count in new_count:
#     if n_count == n_count:


repeated_func(1, 2, 3, 3, 4, 4, 4, 5, 5)
repeated_func1(4, 5, 7, 7, 8, 8, 3, 6, 9, 3, 4, 4, 3, 2, 2, 2)

