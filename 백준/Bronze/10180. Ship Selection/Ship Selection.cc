#include <iostream>
using namespace std;
int main(void) {
    int t,n,d,v,f,c,cnt;
    cin>>t;
    for(int i=0;i<t;i++) {
        cin>>n>>d;
        cnt=0;
        for(int j=0;j<n;j++) {
            cin>>v>>f>>c;
            if(v*f/c>=d)
                cnt+=1;
        }
        cout<<cnt<<"\n";
    }
    return 0;
}