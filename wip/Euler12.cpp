/*
 * Project Euler
 * Problem 12 - Highly divisible triangular number
 * https://projecteuler.net/problem=12
 * Created by Andrew Voss
 */

#include <iostream>
using namespace std;

int findFactors(int x){
  int value = x;
  int i;
  int numberOfDivisor = 0;

  for(i = 1; i <= value; i++){
    if(value % i == 0){
      numberOfDivisor++;
    }
  }
  return numberOfDivisor;
}

int triangleNum(int x){
  int num = 0;
  int i;
  for(i = 0; i <= x; i++){
    num = num + i;
  }
  return num;
}

int main()
{
  /*int x, y, i;
  for(int run = 1; run; i++){
    x = triangleNum(i);
    y = findFactors(x);
    if(y > 500){
      run = 0;
    }
  }

  cout << x << "\n" << y << endl;*/

  cout << triangleNum(10000000) << endl;
  cout << findFactors(16476686400) << endl;
}
