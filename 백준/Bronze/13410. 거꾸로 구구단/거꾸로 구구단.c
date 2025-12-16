#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    int n,k,l,maxn=0;
    char tmp[5],tmp_copy[5];
    scanf("%d %d",&n,&k);
    int arr[k];
    for(int i=0;i<k;i++) {
        sprintf(tmp,"%d",n*(i+1));
        l=strlen(tmp);
        for(int i=0;i<l;i++)
            tmp_copy[i]=tmp[l-1-i];
        tmp_copy[l]='\0';
        arr[i]=atoi(tmp_copy);
        if(maxn<arr[i])
            maxn=arr[i];
    }
    printf("%d",maxn);
    return 0;
}