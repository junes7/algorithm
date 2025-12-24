#include <stdio.h>
int main(void) {
    int a,t,rlt;
    scanf("%d %d",&a,&t);
    rlt=10+2*(25-a+t);
    printf("%d",rlt<0?0:rlt);
    return 0;
}