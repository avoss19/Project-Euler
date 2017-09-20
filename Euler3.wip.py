# Euler 3
# https://projecteuler.net/problem=3
# Created by Andrew Voss

# define variables
PrimeOf = 600851475143
c = []

# find factors
def factor(f):
    i = 1
    a = []
    while i <= f:
        if f%i == 0:
            a.append(i)
        i += 1
    return a

e = len(x) - 1
while e <= len(x):
    d = x[e]
    if factor(d) == [1,d]:
        c.append(d)
        print c
        exit()
    e -= 1
