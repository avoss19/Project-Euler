# Project Euler
# Problem 1 - Multiples of 3 and 5
# https://projecteuler.net/problem=1
# Engineering 2 9.3.3
# Created by Andrew Voss

# create list for multiples of 3 & 5
i = 0
num = []


# add multiples of 3 to list
while i < 1000:
    num.append(i)
    i += 3

# add multiples of 5 to list
d = 0
while d < 1000:
    num.append(d)
    d += 5

# remove duplicate numbers in list
num1 = list(set(num))

# find sum of multiples of 3 & 5
a = sum(num1)

# print the sum
print "Sum of multiples of 3 & 5 below 1000:", a
