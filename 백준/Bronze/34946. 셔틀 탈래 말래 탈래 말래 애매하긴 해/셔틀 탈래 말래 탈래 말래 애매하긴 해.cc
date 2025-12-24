#include <iostream>
using namespace std;
int main(void) {
    int a,b,c,d;
    cin>>a>>b>>c>>d;
    string st;
    if(a+b>d && c>d)
        st="T.T";
    else {
        if(c>d)
            st="Shuttle";
        else if(a+b>d)
            st="Walk";
        else
            st="~.~";
    }
    cout<<st;
    return 0;
}