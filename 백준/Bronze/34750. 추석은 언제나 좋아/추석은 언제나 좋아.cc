#include <iostream>
using namespace std;
int main(void) {
    int n,don,gi;
    cin>>n;
    if(n>=1000000)
        don=n*0.2,gi=n*0.8;
    else if(n>=500000 && n<1000000)
        don=n*0.15,gi=n*0.85;
    else if(n>=100000 && n<500000)
        don=n*0.1,gi=n*0.9;
    else
        don=n*0.05,gi=n*0.95;
    cout<<don<<' '<<gi;
    return 0;
}