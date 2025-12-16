#include <iostream>
#include <cmath>
using namespace std;
int main(void) {
    int r,w,l,cnt=1;
    while(1) {
        cin>>r;
        if(r==0) break;
        cin>>w>>l;
        cout<<"Pizza "<<cnt++<<(2*r>=sqrt(w*w+l*l)?" fits ":" does not fit ")<<"on the table.\n";
    }
    return 0;
}