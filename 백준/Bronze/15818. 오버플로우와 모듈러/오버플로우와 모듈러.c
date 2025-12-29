#include <stdio.h>
#include <stdlib.h>
int main(void) {
    int n,m;
    scanf("%d %d",&n,&m);
    long long rlt=1;
    int *arr=(int*)malloc(sizeof(int)*n);
    for(int i=0;i<n;i++) {
        scanf("%d",&arr[i]);
        rlt*=arr[i];
        rlt%=m;
    }
    printf("%d",rlt);
    return 0;
}