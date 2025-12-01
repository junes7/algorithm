#include <iostream>
using namespace std;
int main(void) {
    int d,e,q;
    char op;
    cin>>d>>e;
    for(int i=0;i<e;i++) {
        cin>>op>>q;
        d=op=='+'?d+q:d-q;
    }
    cout<<d;
    return 0;
}