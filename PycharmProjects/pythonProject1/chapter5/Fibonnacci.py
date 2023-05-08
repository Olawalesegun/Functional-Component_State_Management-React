#(Fibonacci) As seen in Exercise 3.15, the Fibonacci numbers are a sequence in which
#each number is the sum of the two preceding ones. Define a function fib that receives three
#consecutive numbers of the Fibonacci series and returns the three subsequent values. Then,
#call the function three times starting with the numbers 0, 1, and 1 and restarting the func-
#tion each time with the resulting numbers of the previous iteration.
def fib(a, b, c):
    return b, c, b + c

# start with 0, 1, 1
x, y, z = 0, 1, 1
print(x, y, z)

# call fib three times with the previous three values
for i in range(3):
    x, y, z = fib(x, y, z)
    print(x, y, z)