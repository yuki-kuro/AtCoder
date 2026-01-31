#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main()
{
  // 入力
  int n, m, k;
  cin >> n >> m >> k;
  int h[220000];
  rep(i, n) cin >> h[i];
  int b[220000];
  rep(i, m) cin >> b[i];

  // 主処理
  sort(h, h + n);
  sort(b, b + m);
  int count = 0;
  int j = 0;
  rep(i, n)
  {
    for (; j < m; j++)
    {
      if (h[i] <= b[j])
      {
        count++;
        break;
      }
    }
  }

  // 出力
  if (count >= k)
    cout << "Yes" << endl;
  else
    cout << "No" << endl;
}