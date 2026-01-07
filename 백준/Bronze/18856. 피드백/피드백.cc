#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    int n;
    cin >> n;
    vector<int> arr(n, 0);
    arr[0] = 1, arr[1] = 2, arr[n - 1] = 997;
    for (int i = 1; i < n; i++) {
        if (arr[i] == 0)
            arr[i] = arr[i - 1] + 1;
    }
    cout << n << "\n";
    for (int i = 0; i < n; i++)
        cout << arr[i] << ' ';
    return 0;
}