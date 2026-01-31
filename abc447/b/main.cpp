#include <bits/stdc++.h>

#include <algorithm>
#include <string>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  string s;
  cin >> s;
  map<char, int> m;
  for (char c : s) {
    m[c]++;
  }
  int max = -1;
  for (auto p : m) {
    if (max < p.second) {
      max = p.second;
    }
  }
  vector<char> vec = {};
  for (auto p : m) {
    if (p.second == max) {
      vec.push_back(p.first);
    }
  }
  rep(i, vec.size()) { 
    s.erase(std::remove(s.begin(), s.end(), vec.at(i)), s.end());
  }
  cout << s << endl;
}