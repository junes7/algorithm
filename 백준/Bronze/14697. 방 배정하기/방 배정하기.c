#include <stdio.h>
int main(void) {
    int a,b,c,n;
    scanf("%d %d %d %d",&a,&b,&c,&n);
    int dp[301]={0},tar[]={a,b,c};
    dp[a]=dp[b]=dp[c]=1;
    for(int i=a;i<n+1;i++) {
        for(int j=0;j<3;j++) {
            if(i>=tar[j] && dp[i-tar[j]])
                dp[i]=1;
        }
    }
    printf("%d",dp[n]);
    return 0;
}