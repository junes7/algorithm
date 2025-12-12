#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    char *temp,st1[6],st2[6];
    scanf("%s %s",st1,st2);
    int idx=0,t1[2],t2[2];
    temp=strtok(st1,":");
    while(temp!=NULL) {
        t1[idx++]=atoi(temp);
        temp=strtok(NULL,":");
    }
    idx=0;
    temp=strtok(st2,":");
    while(temp!=NULL) {
        t2[idx++]=atoi(temp);
        temp=strtok(NULL,":");
    }
    printf("%s",t1[0]*60+t1[1]<t2[0]*60+t2[1]?"YES":"NO");
    return 0;
}