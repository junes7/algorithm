#include <stdio.h>
int main(void) {
    int n,m,k;
    scanf("%d %d %d",&n,&m,&k);
    printf("%d %d",n-(m*k)<0?0:n-(m*k),n-m*(k-1)-1);
    return 0;
}