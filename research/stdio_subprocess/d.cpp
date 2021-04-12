#include <iostream>

using namespace std;

int main() {
  int temp;
  for (int i = 0; i < 100000; i++)
  {
    cin >> temp;
    cout << "Back: " << temp << endl;
  }
  
  return 0;
}