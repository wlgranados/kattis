#include <iostream>
using namespace std;

int main()
{
    int dataAvailablePerMonth, numMonths;
    cin >> dataAvailablePerMonth;
    cin >> numMonths;
    int totalData = dataAvailablePerMonth * numMonths;
    int totalConsumed = 0;
    for (int i = 0; i < numMonths;i++) {
      int currMonthConsumption;
      cin >> currMonthConsumption;
      totalConsumed += currMonthConsumption;
    }
    int totalForNext = totalData - totalConsumed + dataAvailablePerMonth;
    cout << totalForNext;
}