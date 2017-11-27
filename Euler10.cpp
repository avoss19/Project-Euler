#include <iostream>
using namespace std;

#define MAX 2e6
//define MAX 10 // Value used for testing

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
  int value;
  int x;
  int temp;
  unsigned long long int total;
  total = 0;
  value = MAX;

  for(x = 0; x < value; x++){
    if(checkPrime(x)){
      total = total + x;
      cout << x << " " << total << endl;
    }
  }
  cout << total << endl;
}
