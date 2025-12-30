#include <stdio.h>
int main(void) {
    int n,k;
    scanf("%d %d",&n,&k);
    for(int i=0;i<n-1;i++)
        k/=2;
    printf("%d",k);
    return 0;
}