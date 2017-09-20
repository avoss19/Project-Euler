# Euler 5
# https://projecteuler.net/problem=5
# Created by Andrew Voss

# varaibles
x = 2520 #start
a = []

# Create list numbers 1-20
for w in range(1, 21):
    a.append(w)

while True:
    x += 1
    if (x % any(a)) != 0:
        print "ya"
        print x
        exit()
