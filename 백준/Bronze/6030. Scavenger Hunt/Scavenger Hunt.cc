#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    int p, q;
    cin >> p >> q;
    vector<int> pe, qe;
    for (int i = 1; i < p + 1; i++)
        if (p % i == 0)
            pe.push_back(i);
    for (int i = 1; i < q + 1; i++)
        if (q % i == 0)
            qe.push_back(i);
    for (int i = 0; i < pe.size(); i++) {
        for (int j = 0; j < qe.size(); j++)
            cout << pe[i] << ' ' << qe[j] << "\n";
    }
    return 0;
}