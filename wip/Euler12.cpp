#include <iostream>
using namespace std;

int findFactors(int x){
  int value = x;
  int i;
  int numberOfDivisor = 0;

  for(i = 1; i <= value; value++){
    if(value % i == 0){
      numberOfDivisor = numberOfDivisor + 1;
    }
  }
  return numberOfDivisor;
}

int main()
{
  cout << findFactors(10) << endl;
}
