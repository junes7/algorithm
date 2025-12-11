#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
int main(void) {
    int n,l,cnt=0,idx=0;
    char *ch=(char*)malloc(sizeof(char)*22);
    scanf("%d",&n);
    int rlt[10][11]={
        {1,2,3,4,5,6,7,8,10,12,13},
        {1,3,5,6,7,8,9,12,13},
        {1,3,5,6,7,8,9,12,13},
        {1,2,3,5,6,7,8,12,13},
        {1,3,5,6,7,8,12,13},
        {1,3,5,6,7,8,12,13},
        {1,3,5,6,7,8,12,13},
        {1,3,5,6,7,8,12,13},
        {1,3,5,6,7,8,12,13},
        {1,2,3,6,7,8,12,13}
    };
    l=sizeof(rlt[n-1])/sizeof(int);
    for(int i=0;i<l;i++)
        if(isalpha(rlt[n-1][i]+64)) {
            cnt+=1;
            ch[idx++]=(char)(rlt[n-1][i]+64);
            ch[idx++]=(char)32;
        }
    ch[idx]='\0';
    printf("%d\n%s",cnt,ch);
    return 0;
}