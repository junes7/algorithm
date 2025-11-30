#include <iostream>
using namespace std;
int main(void) {
    int n,m,a,b,rlt;
    cin>>n>>m>>a>>b;
    rlt=n*3-m;
    cout<<(rlt>0?rlt*a+b:0);
    return 0;
}