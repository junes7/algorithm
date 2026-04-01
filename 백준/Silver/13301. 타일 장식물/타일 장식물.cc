#include <iostream>
using namespace std;
int main(void) {
    int n;
    long long a = 1, b = 1, t;
    cin >> n;
    for (int i = 0; i < n - 1; i++) {
        t = a;
        a = b;
        b = b + t;
    }
    cout << (a + b) * 2;
    return 0;
}