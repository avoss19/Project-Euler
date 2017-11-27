/*
a < b < c
a^2+b^2=c^2
a+b+c=1000
*/

#include <iostream>
using namespace std;

bool checkSum1000(int x,int y,int z){
  if(x+y+z==1000)
    return true;
  else
    return false;
}

int findNumBruteForce(){
  int x, y, z;
  x = 0, y=0, z = 0;
  for(x = 0; x < 1000; x++){
    for(y = 0; y < x; y++){
      for(z = 0; z < y; z++){
        if(((x + y + z)==1000) && ((x*x)+(y*y)==(z*z))){
          cout << x << " " << y << " " << z << endl;
        }
      }
    }
  }
  return 0;
}


int main()
{
  findNumBruteForce();
}
