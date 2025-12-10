#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    int n,k,l;
    cin>>n>>k;
    l=n/2+(n%2==0?0:1);
    vector<int> arr(k);
    for(int i=0;i<k;i++) {
        cin>>arr[i];
        cout<<(arr[i]<=l?1:n)<<' ';
    }
    return 0;
}