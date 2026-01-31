#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main()
{
    int N, S;
    cin >> N >> S;
    vector<int> A(N), P(N);
    rep(i, N) cin >> A.at(i);
    rep(i, N) cin >> P.at(i);

    int count = 0;
    rep(i, N)
    {
        rep(j, N)
        {
            if (S == A.at(i) + P.at(j))
            {
                count++;
            }
        }
    }
    cout << count << endl;
}
