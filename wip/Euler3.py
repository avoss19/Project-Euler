# Euler 3
# https://projecteuler.net/problem=3
# Created by Andrew Voss

# Define Variables
MAX = 13195 # Prime Numbers Of

# list for prime testing
a = [2,3,5,7,9,11,13,17,19,29]

e = 0
while e <= 10:
    if (MAX % a[e]) != 0:
        print(a[e])
    e += 1
