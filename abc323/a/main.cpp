#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

// 文字列Lv3
int main() {
    /*
  // forで一文字ずつ確認する解法
  string s;
  cin >> s;
  bool flg = true;
  for (int i = 2; i <= (int)(s.size()); i += 2) {
    if (s[i - 1] == '1') {
      flg = false;
      break;
    }
  }
  if (flg) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
*/
  // ビット演算による解法
  string s;
  cin >> s;
  bitset<16> b(s);
  unsigned int mask = 0b0101010101010101;
  if ((b.to_ulong() & mask) == 0) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
}