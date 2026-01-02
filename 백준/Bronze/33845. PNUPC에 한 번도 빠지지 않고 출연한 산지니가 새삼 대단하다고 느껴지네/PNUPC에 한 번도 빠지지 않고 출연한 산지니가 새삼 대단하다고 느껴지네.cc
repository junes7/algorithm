#include <iostream>
using namespace std;
int main(void) {
    string s, t, rlt = "";
    cin >> s >> t;
    for (int i = 0; i < t.size(); i++) {
        if (s.find(t[i]) == string::npos)
            rlt += t[i];
    }
    cout << rlt;
    return 0;
}