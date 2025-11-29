#include <stdio.h>
#include <stdlib.h>
int main(void) {
    int n,*arr,maxn=0,minn=100;
    scanf("%d",&n);
    arr=(int*)malloc(sizeof(int)*n);
    for(int i=0;i<n;i++) {
        scanf("%d", &arr[i]);
        if(maxn<arr[i])
            maxn=arr[i];
        if(minn>arr[i])
            minn=arr[i];
    }
    printf("%s",minn==arr[0]?"ez":maxn==arr[0]?"hard":"?");
    return 0;
}