#include <iostream>
#include <sstream>
#include <vector>
using namespace std;
int main(void) {
    int cnt = 0, n, idx;
    string st;
    cin >> st >> n;
    vector<int> carr(3), arr(3);
    stringstream ss(st);
    idx = 0;
    while (getline(ss, st, '-')) {
        carr[idx++] = stoi(st);
    }
    for (int i = 0; i < n; i++) {
        idx = 0;
        cin >> st;
        stringstream ss(st);
        while (getline(ss, st, '-')) {
            arr[idx++] = stoi(st);
        }
        if (arr[0] > carr[0]) {
            cnt += 1;
        } else if (arr[0] == carr[0]) {
            if (arr[1] > carr[1])
                cnt += 1;
            else if (arr[1] == carr[1] && arr[2] >= carr[2])
                cnt += 1;
        }
    }
    cout << cnt;
    return 0;
}