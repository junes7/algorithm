#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    int n;
    scanf("%d",&n);
    getchar();
    char *temp;
    char *str=(char*)malloc(sizeof(char)*101);
    char *rlt=(char*)malloc(sizeof(char)*401);
    memset(rlt,0,sizeof(char)*101);
    gets(str);
    temp=strtok(str," ");
    while(temp!=NULL) {
        strcat(rlt,temp);
        strcat(rlt,"DORO ");
        temp=strtok(NULL," ");
    }
    printf("%s",rlt);
    return 0;
}