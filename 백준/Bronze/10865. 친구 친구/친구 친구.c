#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    int n,m,a,b;
    scanf("%d %d",&n,&m);
    int *cnt=(int*)malloc(sizeof(int)*(n+1));
    memset(cnt,0,sizeof(int)*(n+1));
    for(int i=0;i<m;i++) {
        scanf("%d %d",&a,&b);
        cnt[a]+=1;
        cnt[b]+=1;
    }
    for(int i=1;i<n+1;i++)
        printf("%d\n",cnt[i]);
    return 0;
}