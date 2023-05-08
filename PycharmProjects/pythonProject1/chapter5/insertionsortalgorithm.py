import random

# Create a list of 10 unique and randomly picked numbers between 0 and 100
numbers = random.sample(range(101), 10)

print("Unsorted list:", numbers)

sorted_numbers = insertion_sort(numbers)

print("Sorted list:", sorted_numbers)