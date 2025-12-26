#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    int n,d;
    char *st=(char*)malloc(sizeof(char)*11);
    scanf("%d %d",&n,&d);
    for(int i=0;i<n;i++) {
        scanf("%s",st);
        for(int j=0;j<strlen(st);j++) {
            if(st[j]=='d')
                st[j]=d==1?'q':'b';
            else if(st[j]=='b')
                st[j]=d==1?'p':'d';
            else if(st[j]=='q')
                st[j]=d==1?'d':'p';
            else
                st[j]=d==1?'b':'q';
        }
        printf("%s\n",st);
    }
    return 0;
}