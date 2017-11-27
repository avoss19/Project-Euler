def checkPalindrom(x):
    temp = x
    x = str(x)
    length = len(x)
    if length % 2 == 0:
        halfLength = length / 2
        firstHalf = x[0:halfLength]
        secondHalf = x[halfLength:length]
        secondHalf = secondHalf[::-1] # Flip secondHalf
        if firstHalf == secondHalf:
            secondHalf = secondHalf[::-1]
            return True
        else:
            return False
    else:
        return False

def productOf(x):
    for i in xrange(x,0,-1):
        if x % i == 0:
            productP1 = x / i
            strProductP1 = str(productP1)
            strProductP2 = str(i)
            if len(strProductP1) == len(strProductP2):
                #print "Product is", strProductP1, strProductP2
                print "Solution:", int(strProductP1) * int(strProductP2)
                exit()

MAX = 999*999

for x in xrange(MAX, 0, -1):
    if checkPalindrom(x):
        productOf(x)
