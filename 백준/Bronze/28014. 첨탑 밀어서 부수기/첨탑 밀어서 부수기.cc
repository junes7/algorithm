#include <iostream>
using namespace std;
int main(void) {
    int n,prev,cur,rlt=1;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin>>n;
    cin>>prev;
    for(int i=0;i<n-1;i++) {
        cin>>cur;
        if(prev<=cur) rlt+=1;
        prev=cur;
    }
    cout<<rlt;
    return 0;
}