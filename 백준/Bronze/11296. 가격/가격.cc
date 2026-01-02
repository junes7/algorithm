#include <cmath>
#include <iostream>
#include <map>
using namespace std;
int main(void) {
    int n;
    double ori;
    char dot, vou, pri;
    map<char, double> dic = {{'R', 0.55}, {'G', 0.7}, {'B', 0.8}, {'Y', 0.85}, {'O', 0.9}, {'W', 0.95}};
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> ori >> dot >> vou >> pri;
        ori *= dic[dot];
        if (vou == 'C')
            ori *= 0.95;
        ori *= 100;
        if (pri == 'C') {
            if (fmod(ori, 10) > 5) ori += 10;
            ori -= fmod(ori, 10);
        }
        cout << fixed;
        cout.precision(2);
        cout << '$' << ori / 100 << "\n";
    }
    return 0;
}