#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    // map(連想配列)を使用して、1回だけ出現する文字を出力する
  string s;
  cin >> s;
  map<char, int> m;
  for (char c : s) m[c]++;
  char ans = ' ';
  for (auto p : m) {
    if (p.second == 1) {
      ans = p.first;
      break;
    }
  }
  if (ans != ' ') {
    cout << ans << endl;
  } else {
    cout << -1 << endl;
  }
}
