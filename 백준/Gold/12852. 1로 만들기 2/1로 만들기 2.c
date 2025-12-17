#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    int x,tmp,now,idx=0,*dp,*rlt;
    scanf("%d",&x);
    dp=(int*)malloc(sizeof(int)*(x+1));
    memset(dp,0,sizeof(int)*(x+1));
    for(int i=2;i<x+1;i++) {
        dp[i]=dp[i-1]+1;
        if(i%3==0)
            dp[i]=dp[i]<dp[i/3]+1?dp[i]:dp[i/3]+1;
        if(i%2==0)
            dp[i]=dp[i]<dp[i/2]+1?dp[i]:dp[i/2]+1;
    }
    printf("%d\n",dp[x]);
    rlt=(int*)malloc(sizeof(int)*x);
    rlt[idx++]=x;
    tmp=dp[x]-1,now=x;
    for(int i=x;i>=0;i--) {
        if(dp[i]==tmp && (i+1==now || i*3==now || i*2==now)) {
            now=i;
            rlt[idx++]=i;
            tmp-=1;
        }
    }
    for(int i=0;i<idx;i++)
        printf("%d ",rlt[i]);
    return 0;
}