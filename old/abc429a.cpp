#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main()
{
    int n, m;
    cin >> n >> m;
    rep(i, n)
    {
        if (i < m)
            cout << "OK" << endl;
        else
            cout << "Too Many Requests" << endl;
    }
}