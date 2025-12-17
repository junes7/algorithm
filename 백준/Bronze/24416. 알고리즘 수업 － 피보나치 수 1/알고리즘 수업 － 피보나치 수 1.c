#include <stdio.h>
#include <stdlib.h>
int main(void) {
    int n,*fibo;
    scanf("%d",&n);
    fibo=(int*)malloc(sizeof(int)*(n+1));
    fibo[1]=fibo[2]=1;
    for(int i=3;i<n+1;i++)
        fibo[i]=fibo[i-1]+fibo[i-2];
    printf("%d %d",fibo[n],n-2);
    return 0;
}