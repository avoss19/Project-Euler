#include <iostream>
#include <string>
using namespace std;

// Check if divisiable by numbers 1-20
bool dividedByNums(int x){
  bool divisable = false;
  if(x % 20 == 0){
    if(x % 19 == 0){
      if(x % 18 == 0){
        if(x % 17 == 0){
          if(x % 16 == 0){
            if(x % 15 == 0){
              if(x % 14 == 0){
                if(x % 13 == 0){
                  if(x % 12 == 0){
                    if(x % 11 == 0){
                      divisable = true;
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
  return divisable;
}

int main()
{
  bool solutionCheck = true;
  bool check = false;
  int x = 1;
  while(solutionCheck){
    x++;
    check = dividedByNums(x);
    if(check){
      solutionCheck = false;
    }
  }
  cout << x << endl;
}
