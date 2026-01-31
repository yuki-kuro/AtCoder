#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  // 解1.if文で分岐
  /*
    string s;
  cin >> s;
  if (s[0] == s[1] && s[1] == s[2])
    cout << 1 << endl;
  else if (s[0] != s[1] && s[1] != s[2] && s[0] != s[2])
    cout << 6 << endl;
  else
    cout << 3 << endl;
    */
  // 解2. setを使って種類の数を数える。データ構造 重複削除

  string s;
  cin >> s;
  set<char> st;
  for (char c : s) st.insert(c);  // setに格納
  int cnt = st.size();
  if (cnt == 1)
    cout << 1 << endl;
  else if (cnt == 2)
    cout << 3 << endl;
  else
    cout << 6 << endl;
}