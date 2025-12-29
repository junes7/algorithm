#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    int n,m;
    cin>>n>>m;
    long long rlt=1;
    vector<int> arr(n);
    for(int i=0;i<n;i++) {
        cin>>arr[i];
        rlt*=arr[i];
        rlt%=m;
    }
    cout<<rlt;
    return 0;
}