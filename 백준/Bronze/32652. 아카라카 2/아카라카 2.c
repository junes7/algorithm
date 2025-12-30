#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    int n;
    scanf("%d",&n);
    char *st=(char*)malloc(sizeof(char)*210);
    memset(st,0,sizeof(char)*210);
    strcat(st,"AKA");
    for(int i=0;i<n;i++)
        strcat(st,"RAKA");
    printf("%s",st);
    return 0;
}