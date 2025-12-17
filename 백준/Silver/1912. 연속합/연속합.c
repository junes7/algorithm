#include <stdio.h>
#include <stdlib.h>
int main(void) {
    int n,maxn,*num,*dp;
    scanf("%d",&n);
    num=(int*)malloc(sizeof(int)*n);
    dp=(int*)malloc(sizeof(int)*(n+1));
    for(int i=0;i<n;i++)
        scanf("%d",&num[i]);
    dp[0]=num[0];
    maxn=dp[0];
    for(int i=1;i<n;i++) {
        dp[i]=num[i]>(num[i]+dp[i-1])?num[i]:(num[i]+dp[i-1]);
        if(maxn<dp[i]) maxn=dp[i];
    }
    printf("%d",maxn);
    return 0;
}