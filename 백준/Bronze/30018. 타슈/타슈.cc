#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    int n,rlt=0;
    cin>>n;
    vector<int> a(n),b(n);
    for(int i=0;i<n;i++)
        cin>>a[i];
    for(int i=0;i<n;i++) {
        cin>>b[i];
        rlt+=abs(a[i]-b[i]);
    }
    cout<<rlt/2;
    return 0;
}