/*
 * Project Euler
 * Problem 7 - 10001st prime
 * https://projecteuler.net/problem=7
 * Created by Andrew Voss
 */

#include <iostream>
using namespace std;

bool checkPrime(int n)
{
  int i,count=0;

  if(n==1)
    return false;
	if(n==2)
    return true;
  if(n%2==0)
    return false;

  for(i=1;i<=n;i++)
    if(n%i==0)
      count++;
    if(count==2)
      return true;
    else
      return false;
}

int main()
{
  int i = 0;
  int x;
  for(x=2;i<10001;x++){
    if(checkPrime(x)){
      i++;
      cout << x << endl;
    }
  }
}
