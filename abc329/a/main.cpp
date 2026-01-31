#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

// 文字列Lv3
int main() {
  string s;
  cin >> s;
  //   string ans = "";
  //   for (char c : s) {
  //     ans += c + " ";  // " "は文字列のポインタになってしまう
  //   }
  //   cout << ans << endl;

  // for(char c:s){
  // ans += c + string(" "); // これなら連結として動く
  // }

  for (char c : s) {
    cout << c << " ";  // 表示するだけならこれでよい
  }
  cout << endl;
}