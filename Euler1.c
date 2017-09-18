// Euler 1
// https://projecteuler.net/problem=1
// Created by Andrew Voss

/* Current problems:
There are double of numbers
*/

#import <stdio.h>

#define MAX 10 // multiples below

int main()
{
  int total, total3, total5, e, o;
  total = total3 = total5 = e = o = 0;

  while (total3 <  MAX) {
    e += 3;
    total3 += e;
    printf("%d\n", total3);
  }
  while (total5 < MAX) {
    o += 5;
    total5 += o;
    printf("%d\n", total5);
  }
  total = total3 + total5;
  printf("%d\n", total);
}
