#include <iostream>
#include <string>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{
    int numOfInputs;
    cin >> numOfInputs;
    long output = 0;
    for (int i = 0; i < numOfInputs;i++) {
      int initValue;
      cin >> initValue;
      long powerOf = pow(floor(initValue / 10), initValue % 10);
      output += powerOf;
    }
    cout << setprecision(0) << output;
}