#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
int main(void) {
    int x,tmp,now;
    cin>>x;
    vector<int> dp(x+1),rlt;
    for(int i=2;i<x+1;i++) {
        dp[i]=dp[i-1]+1;
        if(i%3==0)
            dp[i]=min(dp[i],dp[i/3]+1);
        if(i%2==0)
            dp[i]=min(dp[i],dp[i/2]+1);
    }
    cout<<dp[x]<<"\n";
    rlt.push_back(x);
    tmp=dp[x]-1,now=x;
    for(int i=x;i>=0;i--) {
        if(dp[i]==tmp && (i+1==now || i*3==now || i*2==now)) {
            now=i;
            rlt.push_back(i);
            tmp-=1;
        }
    }
    for(int i=0;i<rlt.size();i++)
        cout<<rlt[i]<<' ';
    return 0;
}