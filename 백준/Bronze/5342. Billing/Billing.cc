#include <iostream>
#include <map>
using namespace std;
int main(void) {
    string st;
    double rlt = 0;
    map<string, double> sup = {
        {"Paper", 57.99},
        {"Printer", 120.50},
        {"Planners", 31.25},
        {"Binders", 22.50},
        {"Calendar", 10.95},
        {"Notebooks", 11.20},
        {"Ink", 66.95}};
    while (cin >> st)
        rlt += sup[st];
    cout << "$" << rlt;
    return 0;
}