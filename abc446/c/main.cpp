#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int t;
  cin >> t;

  rep(i, t) {
    int n, d;
    cin >> n >> d;
    vector<int> a(n);
    vector<int> b(n);
    queue<int> egg = {};
    rep(j, n) { cin >> a.at(j); }
    rep(j, n) { cin >> b.at(j); }
    rep(j, n) {
      rep(k, a.at(j)) { egg.push(j); }
      rep(k, b.at(j)) { egg.pop(); }
      while (!egg.empty() && egg.front() == j - d) {
        egg.pop();
      }
    }
    cout << egg.size() << endl;
  }
}