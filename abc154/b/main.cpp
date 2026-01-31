#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

// 文字列Lv3
// 文字列生成: string(n, 'c') 、stringクラスのコンストラクタの活用。
int main() {
  string s;
  cin >> s;
  string ans = "";
  rep(i, s.size()) { ans += "x"; }
  // ans = string(s.size(),'x');  計算量はO(N)で同じだが、こちらのほうが高速
  cout << ans << endl;
}