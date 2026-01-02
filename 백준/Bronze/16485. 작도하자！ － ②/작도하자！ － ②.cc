#include <iostream>
using namespace std;
int main(void) {
    int c, b;
    cin >> c >> b;
    if (c % b == 0)
        cout << c / b;
    else {
        cout << fixed;
        cout.precision(6);
        cout << (double)c / b;
    }
    return 0;
}