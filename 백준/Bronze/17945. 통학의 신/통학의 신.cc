#include <iostream>
#include <cmath>
using namespace std;
int main(void) {
    int a,b,rlt=0;
    cin>>a>>b;
    rlt=(int)sqrt(a*a-b);
    if(rlt>0)
        cout<<-a-rlt<<' '<<-a+rlt;
    else
        cout<<-a;
    return 0;
}