#include <stdio.h>
int main(void) {
    int n,m,a,b,rlt;
    scanf("%d %d %d %d",&n,&m,&a,&b);
    rlt=n*3-m;
    printf("%d",rlt>0?rlt*a+b:0);
    return 0;
}