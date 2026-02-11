#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    int c, d, rlt, tmp;
    vector<vector<int>> comp = {{30, 40}, {35, 30}, {40, 20}};
    while (true) {
        cin >> c >> d;
        if (c == 0 && d == 0) break;
        rlt = 100000;
        for (int i = 0; i < 3; i++) {
            tmp = comp[i][0] * c + comp[i][1] * d;
            if (rlt > tmp) rlt = tmp;
        }
        cout << rlt << "\n";
    }
    return 0;
}