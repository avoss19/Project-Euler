# Euler 20
# https://projecteuler.net/problem=20
# Created by Andrew Voss

# main variables
factor = 100 # factorial number
x = 1
total = 1 # running total

while x <= 100:
     total = total * x
     x += 1

x = str(total)
x = (list(x))
x = map(int,x)
print sum(x)
