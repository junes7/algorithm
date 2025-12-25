#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    int n;
    bool rlt=true;
    cin>>n;
    vector<long long> arr(n);
    cin>>arr[0];
    for(int i=1;i<n;i++) {
        cin>>arr[i];
        if(arr[i-1]>=arr[i]) {
            rlt=false;
            break;
        }
    }
    cout<<rlt?1:0;
    return 0;
}