#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    int res = 0;
    for (auto c : S) {
        if (c == '+') ++res;
        else --res;
    }
    cout << res << endl;
}