#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
int main(void) {
    int n,*arr,*rlt;
    scanf("%d",&n);
    arr=(int*)malloc(sizeof(int)*n);
    rlt=(int*)malloc(sizeof(int)*2);
    memset(rlt,0,sizeof(int)*2);
    for(int i=0;i<n;i++) {
        scanf("%d",&arr[i]);
        if(arr[i]%2!=0)
            rlt[0]+=1;
        else
            rlt[1]+=1;
    }
    printf("%d",ceil(n/2.0)==rlt[0] && n/2==rlt[1]?1:0);
    return 0;
}