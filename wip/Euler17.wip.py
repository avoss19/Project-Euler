# Euler 17
# https://projecteuler.net/problem=17
# Updated Versoin
# Created by Andrew Voss

# wip
# works for 1-100

# list number of letters in word
ones = ['',3,3,5,4,4,3,5,5,4] # numbers 1-9 list
tenToNineteen = [3,6,6,8,8,7,7,9,8,8] # numbers 10-19
tens = [6,6,5,5,5,7,6,6] # 20-90 tens
hundred = 7
thousand = 8

def toHundred(x):

    temp = 1
    temp2 = 1

    if x<10:
        return(ones[x])
    if 10<=x<20:
        return(tenToNineteen[x-10])
    if 20 <= x < 100:
        if x % 10 == 0:
            return(tens[(x/10)-2])
        else:
            temp = int(x/10)-2
            temp2 = x%10
            return (tens[temp]+ones[temp2])
    if x == 100:
        return (hundred + 3)

def overHundred(x): # wip



    hundredsPlace = int(x/100) # number in hundreds place
    y = x%100
    getLessHundred = toHundred(y)
    callHundredsPlace = hundred + ones[hundredsPlace]

    return getLessHundred + callHundredsPlace

print overHundred(99)
print "ninety nine"
