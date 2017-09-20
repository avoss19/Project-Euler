# Euler 2
# https://projecteuler.net/problem=2
# Created by Andrew Voss

# define variables
x1 = 1
x2 = 2
temp = 0
total = 0
MAX = 4e6 # Max value

# Fibonacci
while x1 < MAX:
    EvenOrOdd = x1
    if EvenOrOdd % 2 == 0:
        total += EvenOrOdd
    temp = x1
    x1 = x2
    x2 = x2 + temp

print "Solution is:", total
