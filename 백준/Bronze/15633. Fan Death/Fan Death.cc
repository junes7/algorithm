#include <iostream>
using namespace std;
int main(void) {
    int n,rlt=0;
    cin>>n;
    for(int i=1;i<n+1;i++) {
        if(n%i==0)
            rlt+=i;
    }
    cout<<rlt*5-24;
    return 0;
}