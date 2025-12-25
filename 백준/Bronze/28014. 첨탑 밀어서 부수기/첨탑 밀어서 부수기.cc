#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    int n,rlt=1;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin>>n;
    vector<int> arr(n);
    for(int i=0;i<n;i++)
        cin>>arr[i];
    for(int i=0;i<n-1;i++)
        if(arr[i]<=arr[i+1])
            rlt+=1;
    cout<<rlt;
    return 0;
}