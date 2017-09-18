# Project Euler
# Problem 17 - Number letter counts
# https://projecteuler.net/problem=17
# Engineering 2 9.3.3
# version 2.0
# Created by Andrew Voss

# value that needs to be converted to words
x = int(raw_input("What number do you want converted to word form? (1-1000)\n> "))

# list for numbers in words
number_1_to_9 = ["one","two","three","four","five","six","seven","eight","nine"]
number_10_to_19 = ["ten","eleven","tweleve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
number_10s_place = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
hundred = "hundred"
thousand = "thousand"

# 10s place list
d = [10,20,30,40,50,60,70,80,90]

# condense code and make more readable
def print1():
    print "The amount of letters in %s is:" % x, len(x)
    exit()

# for values less than 10
if x <= 9:
    x = number_1_to_9[x-1]
    print1()

# values in between 9 and 100
if 9 < x <= 100:

    #values between 9 and 20
    if x < 20:
        x = number_10_to_19[x-10]
        print1()

    # values between 19 and 100
    if 19 < x <= 100:

        x = int(x)

        # values other than tens in between 19 and 100
        if x == any(d):
            d = str(x)
            value2 = int(d[0])
            value1 = int(d[1])
            d = number_10s_place[value2-2]
            y = number_1_to_9[value1-1]
            print "The number of letters in %s-%s is:" % (d, y), len(d+y)
            exit()

        # if value is 100
        if x == 100:
            print "The number of letters in one hundred is:", len(hundred)

        # tens values
        elif x != any(d):
            d = x / 10
            x = number_10s_place[d-2]
            print1()

        exit()

    exit()

# if value is between 100 and 1000
if 100 < x <= 1000:

    if (x == 200) or (x == 300) or (x == 400) or (x == 500) or (x == 600) or (x == 700) or (x == 800) or (x == 900) :
        y = x / 100
        d = number_1_to_9[y-1]
        print "The amount of letters in %s hundred is:" % d, len(d)+7
        exit()

    elif x < 1000:
        x = str(x)
        value3 = int(x[0])
        value2 = int(x[1])
        value1 = int(x[2])
        x = number_1_to_9[value1-1]
        y = number_10s_place[value2-2]
        z = number_1_to_9[value3-1]
        e = hundred
        print "The number of letters in %s hundred %s-%s is:" % (z, y, x), len(x+y+z+e)

    if x == 1000:
        print thousand

else:
    print "Error: a number 1-1000 was not entered"
