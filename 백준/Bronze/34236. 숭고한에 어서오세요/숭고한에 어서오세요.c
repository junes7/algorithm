#include <stdio.h>
int main(void) {
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++)
        scanf("%d",&arr[i]);
    printf("%d",arr[n-1]+arr[1]-arr[0]);
    return 0;
}