#include <iostream>
using namespace std;
int main(void) {
    int n,prev=1000,rlt=0,tmp;
    cin>>n;
    for(int i=0;i<n;i++) {
        cin>>tmp;
        if(prev>=tmp)
            prev=tmp;
        else
            rlt+=tmp-prev;
    }
    cout<<rlt;
    return 0;
}