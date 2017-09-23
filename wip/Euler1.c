/*
 * Euler 1
 * https://projecteuler.net/problem=1
 * Created by Andrew Voss
 * */

// Problems
// Need to write for loop instead of while (while adds one extra cycle)


#include <stdio.h>
#define MAX 10 // Max value, number to find multiples of 3 and 5


int main()
{
  int x, total3, total5, doubles;
  total3 = total5 = doubles = 0;

  while (total3 < MAX, total3++3){
    if (total3 % 5 == 0){
      doubles = doubles - total3;
    }
  }

  while (total5 < MAX){
    total5 = total5 + 5;
  }
  printf ("%d %d %d", total3, total5, doubles);
  x = total5 + total3 - doubles;

  printf ("%d\n", x);
}
