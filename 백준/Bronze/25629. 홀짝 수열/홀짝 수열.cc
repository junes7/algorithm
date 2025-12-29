#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
int main(void) {
    int n;
    cin>>n;
    vector<int> arr(n),rlt(2);
    for(int i=0;i<n;i++) {
        cin>>arr[i];
        if(arr[i]%2!=0)
            rlt[0]+=1;
        else
            rlt[1]+=1;
    }
    cout<<(ceil(n/2.0)==rlt[0] && n/2==rlt[1]?1:0);
    return 0;
}