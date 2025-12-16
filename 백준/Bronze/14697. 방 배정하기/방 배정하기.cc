#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    int a,b,c,n;
    cin>>a>>b>>c>>n;
    vector<int> dp(301),tar={a,b,c};
    dp[a]=dp[b]=dp[c]=1;
    for(int i=a;i<n+1;i++) {
        for(int j=0;j<3;j++) {
            if(i>=tar[j] && dp[i-tar[j]])
                dp[i]=1;
        }
    }
    cout<<dp[n];
    return 0;
}