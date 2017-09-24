/*
 * Euler 1
 * https://projecteuler.net/problem=1
 * Created by Andrew Voss
 * */

// Problems
// Need to write for loop instead of while (while adds one extra cycle)


#include <stdio.h>
#define MAX 1000 // Max value, number to find multiples of 3 and 5


int main()
{
  // Define variables
  int count3, count5, total3, total5, doubles;
  total3 = doubles = 0;

  // Add duplicate multiples to variable "doubles" and find sum of multiples of 3
  for (count3 = 0; count3 < MAX; count3 = count3 + 3){
    total3 = count3 + total3;
    if (count3 % 5 == 0){
      doubles = doubles + count3;
    }
  }

  // find sum of multiples of 5
  for (count5 = 0; count5 < MAX; count5 = count5 + 5)
      total5 = count5 + total5;

  printf("%d\n", total3 + total5 - doubles);
}
