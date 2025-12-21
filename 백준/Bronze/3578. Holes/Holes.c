#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    int h,idx=0;
    char *st=(char*)malloc(sizeof(char)*500);
    memset(st,0,sizeof(char)*500);
    scanf("%d",&h);
    if(h<2) {
        printf("%d",!h);
    } else {
        for(int i=0;i<h%2;i++)
            st[idx++]='4';
        for(int i=0;i<h/2;i++)
            st[idx++]='8';
        printf("%s",st);
    }
    return 0;
}