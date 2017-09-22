# Euler 20
# https://projecteuler.net/problem=20
# Created by Andrew Voss

# main variables
factor = 100 # factorial number
x = 1
total = 1 # running total

# find factorial
while x <= factor:
     total = total * x
     x += 1

# find sum of digits of factorial and print
x = str(total)
x = (list(x))
x = map(int,x)
print sum(x)
