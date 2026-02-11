#include <iostream>
using namespace std;
int main(void) {
    int t;
    string st;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> st;
        while (st.find("PO") != string::npos) {
            st.replace(st.find("PO"), 2, "PHO");
        }
        cout << st << "\n";
    }
    return 0;
}