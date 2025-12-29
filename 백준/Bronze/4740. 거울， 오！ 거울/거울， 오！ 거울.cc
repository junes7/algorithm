#include <iostream>
#include <algorithm>
using namespace std;
int main(void) {
    string st;
    while(getline(cin,st)) {
        if(st=="***") break;
        reverse(st.begin(),st.end());
        cout<<st<<"\n";
    }
    return 0;
}