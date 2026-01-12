#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    int a, b;
    vector<long long> rlt(2, 1);
    cin >> a >> b;
    for (int i = 0; i < b; i++) {
        rlt[0] += a - 2;
        rlt[1] += rlt[0];
    }
    cout << rlt[1];
    return 0;
}