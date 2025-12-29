#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    char ch,*st=(char*)malloc(sizeof(char)*81); 
    int n,idx=0;
    while(gets(st)!=NULL) {
        if(strstr(st,"***")) break;
        n=strlen(st);
        for(int i=0;i<n/2;i++) {
            ch=st[i];
            st[i]=st[n-1-i];
            st[n-1-i]=ch;
        }
        st[n]='\0';
        printf("%s\n",st);
    }
    return 0;
}