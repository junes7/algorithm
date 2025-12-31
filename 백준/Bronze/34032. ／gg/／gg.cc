#include <algorithm>
#include <iostream>
using namespace std;
int main(void) {
    int n, mid;
    string st;
    cin >> n >> st;
    mid = n / 2 + (n % 2 == 0 ? 0 : 1);
    cout << (count(st.begin(), st.end(), 'O') >= mid ? "Yes" : "No");
    return 0;
}