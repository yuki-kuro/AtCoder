/*
#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  string s, t;
  cin >> s >> t;
  //
s,tから'A'をすべて削除して、一致しないなら-1を表示。一致するなら最小値を表示
  // e_s,e_tから'A'をすべて削除
  string e_s = s;
  string e_t = t;
  e_s.erase(std::remove(e_s.begin(), e_s.end(), 'A'), e_s.end());
  e_t.erase(std::remove(e_t.begin(), e_t.end(), 'A'), e_t.end());
  // e_s,e_tが等しいかチェック
  if (e_s != e_t) {
    cout << -1 << endl;
  } else {
    // e_sとe_tが等しくないときはansは0以上
    int ans = 0;


    // sとtは逆だったとしても回数は変わらない
    // s=AAAWAZAAAABAAAU
    // t=AWAAZABAAAAAUA
    // の場合を考え、Aの数を数値に置き換えると
    // s = 3W1Z4B3U
    // t = 1W2Z1B5U1
    // となり、|3-1|+|1-2|+|4-1|+|3-5|+|0-1| = 9が成り立つ
    // 先頭から順にAの出現回数を数え差の絶対値を求める。
    // A以外の文字が出たら次に進む
    // これを最後まで行う


string rep_s = "";
string rep_t = "";
int cnt_s = 0;
int cnt_t = 0;
rep(i, s.size()) {
  if (s.at(i) == 'A') {
    cnt_s++;
  } else {
    rep_s += to_string(cnt_s) + s.at(i);
    cnt_s = 0;
  }
  if (i == s.size() - 1) {
    rep_s += to_string(cnt_s);
  }
}
rep(i, t.size()) {
  if (t.at(i) == 'A') {
    cnt_t++;
  } else {
    rep_t += to_string(cnt_t) + t.at(i);
    cnt_t = 0;
  }
  if (i == t.size() - 1) {
    rep_t += to_string(cnt_t);
  }
}
rep(i, rep_s.size()) {
  if (i % 2 == 0) {
    ans += abs(int(rep_s.at(i)) - int(rep_t.at(i)));
  }
}
cout << ans << endl;
// cout << rep_s << endl;
// cout << rep_t << endl;
}

// 不変量に着目するが、不変量を『壁』や『区切り』として捉え、
// その間に挟まれた可変量『変化するもの（Aの個数）』だけを抽出する、と考える

}
*/

#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

auto removeA(string x) {
  string r;
  for (char c : x) {
    if (c != 'A') {
      r += c;
    }
  }
  return r;
}

auto f(string x) {
  vector<int> v = {0};
  for (char c : x) {
    if (c == 'A') {
      v.back()++;
    } else {
      v.push_back(0);
    }
  }
  return v;
}

int main() {
  string s, t;
  cin >> s >> t;
  if (removeA(s) != removeA(t)) {
    cout << -1 << endl;
    return 0;
  }
  vector<int> a = f(s);
  vector<int> b = f(t);
  int ans = 0;
  rep(i, a.size()) { ans += abs(a.at(i) - b.at(i)); }
  cout << ans << endl;

  return 0;
}