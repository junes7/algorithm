#include <stdio.h>
int main(void) {
    int n,m;
    scanf("%d %d",&n,&m);
    printf("%d",n/m+(n%m==0?0:1));
    return 0;
}