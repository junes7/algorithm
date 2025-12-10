#include <stdio.h>
int main(void) {
    int n,k,l;
    scanf("%d %d",&n,&k);
    l=n/2+(n%2==0?0:1);
    int arr[k];
    for(int i=0;i<k;i++) {
        scanf("%d",&arr[i]);
        printf("%d ",arr[i]<=l?1:n);
    }
    return 0;
}