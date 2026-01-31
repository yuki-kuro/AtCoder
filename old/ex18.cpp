#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int N, M;
  cin >> N >> M;
  vector<int> A(M), B(M);
  rep(i, M) cin >> A.at(i) >> B.at(i);

  vector<vector<char>> R(N, vector<char>(N, '-'));
  rep(i, M) {
    A.at(i)--;
    B.at(i)--;
    R.at(A.at(i)).at(B.at(i)) = 'o';
    R.at(B.at(i)).at(A.at(i)) = 'x';
  }
  rep(i, N) {
    rep(j, N) {
      cout << R.at(i).at(j);
      if (j == N - 1) {
        cout << endl;
      } else {
        cout << " ";
      }
    }
  }
}
