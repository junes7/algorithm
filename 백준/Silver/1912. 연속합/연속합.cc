#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(void) {
    int n;
    cin>>n;
    vector<int> num(n),dp(n+1,-1000);
    for(int i=0;i<n;i++)
        cin>>num[i];
    dp[0]=num[0];
    for(int i=1;i<n;i++) {
        dp[i]=max(num[i],num[i]+dp[i-1]);
    }
    cout<<*max_element(dp.begin(),dp.end());
    return 0;
}