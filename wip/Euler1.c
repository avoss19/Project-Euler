/*
 * Euler 1
 * https://projecteuler.net/problem=1
 * Created by Andrew Voss
 * */

#include <stdio.h>
#define MAX 10 // Max value, number to find multiples of 3 and 5


int main()
{
  int x, total3, total5, doubles;
  x = 1;
  total3 = total5 = doubles = 0;

  while (x < MAX){
    total3 = total3 + 3;

    if (total3 % 5 == 0){
      doubles = doubles - total3;
    }
    x++;
  }

  x = 1;
  while (total5 < MAX){
    total5 = total5 + 5;
    x++;
  }
  printf ("%d %d %d", total3, total5, doubles);
  x = total5 + total3 - doubles;

  printf ("%d\n", x);
}
