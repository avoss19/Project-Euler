# Euler 2
# https://projecteuler.net/problem=2
# Created by Andrew Voss

# define variables
MAX = 4e6 # Fibonacci max value
x1 = 1 # first fibonacci number
x2 = 2 # second fibonacci
temp = total = 0

# Fibonacci
while x1 < MAX:
    # add even number fibonacci
    if x1 % 2 == 0:
        total += x1
    # add next fibonacci number
    temp = x1
    x1 = x2
    x2 = x2 + temp

print "Solution is:", total
