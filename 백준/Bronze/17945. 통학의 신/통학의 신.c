#include <stdio.h>
#include <math.h>
int main(void) {
    int a,b,rlt=0;
    scanf("%d %d",&a,&b);
    rlt=(int)sqrt(a*a-b);
    if(rlt>0)
        printf("%d %d",-a-rlt,-a+rlt);
    else
        printf("%d",-a);
    return 0;
}