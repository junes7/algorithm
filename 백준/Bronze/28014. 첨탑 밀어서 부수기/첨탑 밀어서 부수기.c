#include <stdio.h>
int main(void) {
    int n,rlt=1;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++)
    scanf("%d",&arr[i]);
    for(int i=0;i<n-1;i++)
        if(arr[i]<=arr[i+1])
            rlt+=1;
    printf("%d",rlt);
    return 0;
}