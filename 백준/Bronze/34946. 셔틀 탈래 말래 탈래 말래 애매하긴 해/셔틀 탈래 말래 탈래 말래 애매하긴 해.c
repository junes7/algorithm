#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    int a,b,c,d;
    scanf("%d %d %d %d",&a,&b,&c,&d);
    char *st=(char*)malloc(sizeof(char)*8);
    memset(st,0,sizeof(char)*8);
    if(a+b>d && c>d)
        strcat(st,"T.T");
    else {
        if(c>d)
            strcat(st,"Shuttle");
        else if(a+b>d)
            strcat(st,"Walk");
        else
            strcat(st,"~.~");
    }
    printf("%s",st);
    return 0;
}