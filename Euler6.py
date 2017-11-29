# Project Euler
# Problem 6 - Sum square difference
# https://projecteuler.net/problem=6
# Created by Andrew Voss

sp = "-" * 40

# get value
print sp
print """This will let you find the difference between the sum1 and sum2
1^2 + 2^2 + ... n^2 = sum1
(1 + 2 + ... + n)^2 = sum2"""
e = int(raw_input("What value would like to test?\n> "))

# Create list with numbers 1-n
a = []

i = 1

while i <= e:
    a.append(i)
    i += 1

# Create second list with numbers 1-10
b = a

# sum of "a" and square it
# The square of the sum of the first ten natural numbers
a = sum(a) ** 2

# square each number then add
# The sum of the squares of the first ten natural numbers
b = [ int(x**2) for x in b ]
b = sum(b)

print "The sum of the first equation is:", b
print "The sum of the second equation is:", a
print "The difference is:", [a-b]
