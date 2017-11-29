# Project Euler
# Problem 17 - Number letter counts
# https://projecteuler.net/problem=17
# Created by Andrew Voss

# wip

# works for 1-100

total = 0 # Running total
wordNumbers = 99 # Variable number to get number of letters in word form

# list number of letters in word
ones = ['',3,3,5,4,4,3,5,5,4] # numbers 1-9 list
tenToNineteen = [3,6,6,8,8,7,7,9,8,8] # numbers 10-19
tens = [6,6,5,5,5,7,6,6] # 20-90 tens
hundred = 7
thousand = 8

def toHundred(x): # def for numbers less then or equal to 100

    temp = 1 # temp variables, gets reasigned
    temp2 = 1

    if x<10:
        return(ones[x])
    if 10<=x<20:
        return(tenToNineteen[x-10])
    if 20 <= x < 100:
        if x % 10 == 0: # tens values 20-90
            return(tens[(x/10)-2])
        else: # values 21-99
            temp = int(x/10)-2
            temp2 = x%10
            return (tens[temp]+ones[temp2])
    if x == 100:
        return (hundred + 3)

def overHundred(x): # wip
    if x % 100 == 0:
        return ones[x] + hundred
    if x == 1000:
        return thousand + 3
    else:
        hundredsPlace = int(x/100)
        lessThenHundred = int(x % 100)
        hundredsPlace = ones[hundredsPlace]
        lessThenHundred = toHundred(lessThenHundred)
        return(hundredsPlace+lessThenHundred+7)

print toHundred(99)

for x in range (1, 1001):
    if x <= 100:
        total += toHundred(x)
    if 1000 > x > 100:
        total += overHundred(x)
    if x == 1000:
        total += thousand

print total
