#include <iostream>
using namespace std;
int main(void) {
    int t,n;
    string st;
    cin>>t;
    for(int i=0;i<t;i++) {
        cin>>n;
        for(int j=0;j<n;j++) {
            st="";
            for(int k=0;k<n;k++) {
                if(k==0 || k==n-1)
                    st+='#';
                else {
                    if(1<=j && j<=n/2) {
                        if(k==j || k==n-1-j)
                            st+='#';
                        else
                            st+='.';
                    } else {
                        st+='.';
                    }
                }
            }
            cout<<st<<"\n";
        }
    }
}