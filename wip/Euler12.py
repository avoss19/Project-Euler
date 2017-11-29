# Project Euler
# Problem 12 - Highly divisible triangular number
# https://projecteuler.net/problem=12
# Created by Andrew Voss

def findFactors(x):
    numberOfDivisor = 0
    for i in xrange(1,x+1):
        if x % i == 0:
            numberOfDivisor = numberOfDivisor + 1
    return numberOfDivisor

def valuesOfTriangleNums(x):
    total = 0
    for i in range(1,x+1):
        total = total + i
        i = i + 1
    return total

def main():
    x = 1
    while True:
        temp1 = valuesOfTriangleNums(x)
        temp = findFactors(temp1)
        if temp > 500:
            print temp1
            exit()
        x = x + 1

main()
