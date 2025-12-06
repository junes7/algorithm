#include <iostream>
using namespace std;
int main(void) {
    int n,w,rlt;
    cin>>n>>w;
    rlt=n*10;
    if(n==5)
        rlt+=70;
    else if(n>=3)
        rlt+=20;
    if(w>1000)
        rlt=rlt-15<0?0:rlt-15;
    cout<<rlt;
    return 0;
}