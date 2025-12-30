#include <iostream>
using namespace std;
int main(void) {
    int n,rlt=0;
    string a,b;
    cin>>n>>a>>b;
    for(int i=0;i<n;i++) {
        if(a[i]!=b[i])
            rlt+=1;
    }
    cout<<rlt;
    return 0;
}