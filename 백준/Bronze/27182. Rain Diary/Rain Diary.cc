#include <iostream>
using namespace std;
int main(void) {
    int n, m;
    cin >> n >> m;
    cout << (n >= 8 ? n - 7 : m + 7);
    return 0;
}