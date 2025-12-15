#include <stdio.h>
#include <string.h>
int main(void) {
    int tar,idx,arr[50];
    char rlt[3];
    for(int i=0;i<50;i++)
        scanf("%d",&arr[i]);
    scanf("%d",&tar);
    for(int i=0;i<50;i++) {
        if(arr[i]==tar) {
            idx=i+1;
            break;
        }
    }
    if(idx<=5)
        strcpy(rlt,"A+");
    else if(idx<=15)
        strcpy(rlt,"A0");
    else if(idx<=30)
        strcpy(rlt,"B+");
    else if(idx<=35)
        strcpy(rlt,"B0");
    else if(idx<=45)
        strcpy(rlt,"C+");
    else if(idx<=48)
        strcpy(rlt,"C0");
    else
        strcpy(rlt,"F");
    printf("%s",rlt);
    return 0;
}