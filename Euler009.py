# Project Euler
# Problem 9 - Special Pythagorean triplet
# https://projecteuler.net/problem=9
# Created by Andrew Voss

def solution():
    for z in range(0, 1000):
        for y  in range(0, z):
            for x in range(0, y):
                if(x+y+z==1000) and ((x*x)+(y*y)==(z*z)):
                    return x*y*z

print solution()
