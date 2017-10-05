include <iostream>

using namespace std;

void divisible_by_3()
{
  return (x % 3 == 0);
}

void divisible_by_5()
{
  return 0;
}

int main()
{
  int x = 10;

  cout << divisible_by_3(x) << endl;

  return 0;
}
