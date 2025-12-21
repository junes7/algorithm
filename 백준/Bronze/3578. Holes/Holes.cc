#include <iostream>
using namespace std;
int main(void) {
    int h;
    string st;
    cin>>h;
    if(h<2)
        st=to_string(!h);
    else {
        for(int i=0;i<h%2;i++)
            st+='4';
        for(int i=0;i<h/2;i++)
            st+='8';
    }
    cout<<st;
    return 0;
}