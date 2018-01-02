# Project Euler
# Problem 3 - Largest prime factor
# https://projecteuler.net/problem=3
# Created by Andrew Voss

# Define Variables
factor = 600851475143 # Prime Numbers Of

i = 2
while i * i < factor:
    while factor % i == 0:
        factor = factor / i
    i = i + 1
print factor
