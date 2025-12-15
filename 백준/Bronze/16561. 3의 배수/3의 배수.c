#include <stdio.h>
int main(void) {
    int n;
    scanf("%d",&n);
    n/=3;
    printf("%d",(n-1)*(n-2)/2);
    return 0;
}