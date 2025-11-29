#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    int n,maxn=0,minn=100;
    cin>>n;
    vector<int> arr(n);
    for(int i=0;i<n;i++) {
        cin>>arr[i];
        if(maxn<arr[i])
            maxn=arr[i];
        if(minn>arr[i])
            minn=arr[i];
    }
    cout<<(minn==arr[0]?"ez":(maxn==arr[0]?"hard":"?"));
    return 0;
}