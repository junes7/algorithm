#include <iostream>
using namespace std;
int main(void) {
    int n, p;
    long long rlt = 1;
    cin >> n >> p;
    for (int i = 2; i < n + 1; i++)
        rlt = rlt * i % p;
    cout << rlt;
    return 0;
}