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
  int x1, x2, temp, total;
  x1 = 1; // first fibonacci number (not really, but first need fibonacci number)
  x2 = 2; // second fibonacci
  temp = total = 0;

  // Fibonacci
  while (x1 < MAX){
    // add even number fibonacci
    if (x1 % 2 == 0) {
      total = total + x1;
    }
    // add next fibonacci number
    temp = x1;
    x1 = x2;
    x2 = x2 + temp;
  }

  printf("Solution is: %d\n", total);
}
