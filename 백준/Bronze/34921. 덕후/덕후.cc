#include <iostream>
using namespace std;
int main(void) {
    int a,t,rlt;
    cin>>a>>t;
    rlt=10+2*(25-a+t);
    cout<<(rlt<0?0:rlt);
    return 0;
}