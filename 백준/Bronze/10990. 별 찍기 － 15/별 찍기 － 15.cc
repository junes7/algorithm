#include <iostream>
using namespace std;
int main(void) {
    int n;
    cin >> n;
    for (int i = 0; i < n - 1; i++)
        cout << ' ';
    cout << "*\n";
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 2 - i; j++)
            cout << ' ';
        cout << "*";
        for (int j = 0; j < i * 2 + 1; j++)
            cout << ' ';
        cout << "*\n";
    }
    return 0;
}