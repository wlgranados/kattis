#include <iostream>
#include <string>
using namespace std;

int main()
{
  string input;
  string leftPass, rightPass;
  cin >> input;
  int wordLen = input.size() / 3;
  leftPass = input.substr(0, wordLen);
  rightPass = input.substr(input.size()-wordLen, wordLen);
  if (leftPass == rightPass) {
      cout << leftPass << endl;
  } else {
      cout << input.substr(wordLen, wordLen) << endl;
  }
}