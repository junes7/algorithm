#include <iostream>
using namespace std;
int main(void) {
    int n,m;
    cin>>n>>m;
    for(int i=0;i<n;i++) {
        for(int j=1;j<m+1;j++) {
            cout<<i*m+j;
            if(j!=m) cout<<' ';
        }
        cout<<"\n";
    }
    return 0;
}