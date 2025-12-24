#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    int k,n,m,cnt=0;
    cin>>k>>n;
    vector<int> a(n);
    for(int i=0;i<n;i++)
        cin>>a[i];
    cin>>m;
    vector<int> b(m);
    for(int i=0;i<m;i++)
        cin>>b[i];
    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            if(a[i]+k==b[j])
                cnt+=1;
        }
    }
    cout<<cnt;
    return 0;
}