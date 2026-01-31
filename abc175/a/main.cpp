#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  string s;
  cin >> s;
  int cnt = 0;

  if (s == "RRR") {
    cout << 3 << endl;
  } else if (s == "RRS" || s == "SRR") {
    cout << 2 << endl;
  } else if (s == "SSS") {
    cout << 0 << endl;
  } else {
    cout << 1 << endl;
  }
}