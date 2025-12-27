#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
int main(void) {
    int n,maxn=0,idx;
    int *arr=(int*)malloc(sizeof(int)*3);
    memset(arr,0,sizeof(int)*3);
    char *st=(char*)malloc(sizeof(char)*(pow(10,5)+1));
    char tar[]="BSA";
    scanf("%d %s",&n,st);
    for(int i=0;i<strlen(tar);i++) {
        for(int j=0;j<strlen(st);j++) {
            if(st[j]==tar[i])
                arr[i]+=1;
        }
        if(maxn<arr[i]) maxn=arr[i];
    }
    memset(st,0,sizeof(char)*(pow(10,5)+1));
    if(arr[0]==arr[1] && arr[1]==arr[2] && arr[0]==arr[2])
        strcat(st,"SCU");
    else {
        idx=0;
        for(int i=0;i<3;i++)
            if(arr[i]==maxn)
                st[idx++]=tar[i];
        st[idx]='\0';
    }
    printf("%s",st);
    return 0;
}