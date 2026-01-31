#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

// 文字列Lv3
int main() {
  string s;
  cin >> s;
  // 1文字ずつ変換する解法（速いO(N)）
  /*
  rep(i, s.size()) {
    if (s[i] == '0') {
      cout << '1';
    } else {
      cout << '0';

    }
  }
  cout << endl;
*/
  // replace()を使う解法(遅いO(3N)）
  replace(s.begin(), s.end(), '0', 'x');
  replace(s.begin(), s.end(), '1', '0');
  replace(s.begin(), s.end(), 'x', '1');
  cout << s << endl;
}