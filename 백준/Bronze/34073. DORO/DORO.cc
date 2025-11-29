#include <iostream>
#include <sstream>
using namespace std;
int main(void) {
    int n;
    string st;
    cin>>n;
    getline(cin,st);
    getline(cin,st);
    stringstream ss(st);
    while(getline(ss,st,' ')) {
        cout<<st+"DORO ";
    }
    return 0;
}