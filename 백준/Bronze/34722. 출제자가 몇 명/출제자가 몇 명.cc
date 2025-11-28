#include <iostream>
using namespace std;
int main(void) {
    int n,si,ci,ai,ri,cnt=0;
    cin>>n;
    for(int i=0;i<n;i++) {
        cin>>si>>ci>>ai>>ri;
        if(si>=1000 || ci>=1600 || ai>=1500 || (1<=ri&&ri<=30))
            cnt+=1;
    }
    cout<<cnt;
    return 0;
}