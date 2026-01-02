#include <iostream>
using namespace std;
int main(void) {
    int n, x;
    cin >> n >> x;
    double tmp = n * (1 - x / 100.0);
    cout << fixed;
    cout.precision(6);
    cout << (n / tmp - 1) * 100;
    return 0;
}