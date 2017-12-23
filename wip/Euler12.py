# Project Euler
# Problem 12 - Highly divisible triangular number
# https://projecteuler.net/problem=12
# Created by Andrew Voss

currentRunNum = 0

def findFactors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))) # factors

def valuesOfTriangleNums():
    global currentRunNum
    x = currentRunNum
    total = 0
    for i in range(1,x+1):
        total = total + i
        i = i + 1
    currentRunNum += 1
    return total

def main():
    run = 1
    e = 1
    while run:
        x = valuesOfTriangleNums()
        y = findFactors(x)
        if y > 5:
            run = 0
        e += 1;
        print x, y
    print x, y

print findFactors(224)
