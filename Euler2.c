/*
 * Euler 2
 * https://projecteuler.net/problem=2
 * Created by Andrew Voss
 * Manual port of my Euler 2 from .py
*/

#include <stdio.h>

#define MAX 4e6 // Fibonacci max value

int main()
{
  int x1, x2, temp, total, EvenOrOdd;
  x1 = 1;
  x2 = 2;
  temp = total = 0;

  while (x1 < MAX){
    EvenOrOdd = x1;
    if (EvenOrOdd % 2 == 0) {
      total = total + EvenOrOdd;
    }
    temp = x1;
    x1 = x2;
    x2 = x2 + temp;
  }

  printf("%d\n", total);
}
