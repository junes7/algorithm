#include <cmath>
#include <iostream>
using namespace std;
int main(void) {
    int t, n;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> n;
        double t = sqrt(n);
        cout << (t == (int)t ? 1 : 0) << "\n";
    }
    return 0;
}