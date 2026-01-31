#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

// 文字列Lv3
int main() {
    string o,e;
    cin >>o>>e;
    int n = o.size()+e.size();
    for (int i =0;i<(int)(n-2);i++){
        cout<<o[i]<<e[i];
    }
    cout<<endl;
}