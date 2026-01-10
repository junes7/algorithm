#include <cmath>
#include <iostream>
using namespace std;
int main(void) {
    int st, n1, n2;
    cin >> st;
    while (true) {
        n1 = st / 100, n2 = st % 100 + 1;
        st += 1;
        if (st > 9999) {
            cout << -1;
            break;
        }
        if (st == pow(n1 + n2, 2)) {
            cout << st;
            break;
        }
    }
    return 0;
}