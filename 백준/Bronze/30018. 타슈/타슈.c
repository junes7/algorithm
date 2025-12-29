#include <stdio.h>
#include <stdlib.h>
int main(void) {
    int n,rlt=0,*a,*b;
    scanf("%d",&n);
    a=(int*)malloc(sizeof(int)*n);
    b=(int*)malloc(sizeof(int)*n);
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(int i=0;i<n;i++) {
        scanf("%d",&b[i]);
        rlt+=abs(a[i]-b[i]);
    }
    printf("%d",rlt/2);
    return 0;
}