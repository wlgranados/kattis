#include <iostream>
#include <string>
using namespace std;

int main()
{
  int inp;
  cin >> inp;
  if (inp % 2 == 0) {
      cout << "Bob" << endl;
  } else {
      cout << "Alice" << endl;
  }
}
