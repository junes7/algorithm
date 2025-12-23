#include <iostream>
using namespace std;
int main(void) {
    int d1,d2,d3;
    double sumn,a,b,c;
    cin>>d1>>d2>>d3;
    sumn=(d1+d2+d3)/2.0;
    a=sumn-d3;
    b=sumn-d2;
    c=sumn-d1;
    cout<<fixed;
    cout.precision(1);
    if(a>0 && b>0 &&c>0) {
        cout<<1<<"\n";
        cout<<a<<' '<<b<<' '<<c;
    } else
        cout<<-1;
    return 0;
}