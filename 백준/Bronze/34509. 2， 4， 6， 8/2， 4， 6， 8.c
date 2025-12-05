#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    char ch,st[3],st_copy[3];
    int n;
    for(int i=10;i<50;i++) {
        sprintf(st,"%d",i);
        strcpy(st_copy,st);
        ch=st_copy[0];
        st_copy[0]=st_copy[1];
        st_copy[1]=ch;
        if(st[0]!='8' && st[1]!='8') {
            if((st[0]-48+st[1]-48)%6==0 && atoi(st_copy)%4==0) {
                printf("%d",i);
                break;
            }
        }
    }
    return 0;
}