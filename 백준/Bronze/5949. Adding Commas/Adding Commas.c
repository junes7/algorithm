#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    int n,cnt=0,idx=0,tmp;
    char *st=(char*)malloc(sizeof(char)*11);
    char *rlt=(char*)malloc(sizeof(char)*14);
    scanf("%s",st);
    for(int i=strlen(st)-1;i>=0;i--) {
        if(cnt-3==0) {
            rlt[idx++]=',';
            cnt=0;
        }
        rlt[idx++]=st[i];
        cnt++;
    }
    rlt[idx]='\0';
    for(int i=0;i<idx/2;i++) {
        tmp=rlt[i];
        rlt[i]=rlt[idx-1-i];
        rlt[idx-1-i]=tmp;
    }
    printf("%s",rlt);
    return 0;
}