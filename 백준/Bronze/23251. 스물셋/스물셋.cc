#include <iostream>
using namespace std;
int main(void) {
    int t,k;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin>>t;
    for(int i=0;i<t;i++) {
        cin>>k;
        cout<<23*k<<"\n";
    }
    return 0;
}