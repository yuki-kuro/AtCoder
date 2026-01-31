#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main()
{
    // 入力
    int a, b, c, d;
    cin >> a >> b >> c >> d;

    // 主処理
    bool flg = false;
    if (c >= a)
    {
        if (b > d)
        {
            flg = true;
        }
        else
        {
            flg = false;
        }
    }
    else
    {
        flg = false;
    }

    // 出力
    if (flg)
        cout << "Yes" << endl;
    else
        cout << "No" << endl;
}