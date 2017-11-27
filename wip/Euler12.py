def findFactors(x):
    numberOfDivisor = 0
    for i in xrange(1,x+1):
        if x % i == 0:
            numberOfDivisor = numberOfDivisor + 1
    return numberOfDivisor

x = 1

while True:
    temp = findFactors(x)
    x = x + 1
    if temp > 5:
        print x
        exit()
