#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    vector<int> arr(4);
    for (int i = 0; i < 4; i++)
        cin >> arr[i];
    arr[0] += arr[3];
    arr[1] += arr[2] * 2;
    cout << min(arr[0] / 3, arr[1] / 6);
    return 0;
}