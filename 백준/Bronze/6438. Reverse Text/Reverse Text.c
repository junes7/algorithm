#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    int n,len;
    char ch,*st=(char*)malloc(sizeof(char)*71);
    scanf("%d",&n);
    getchar();
    for(int i=0;i<n;i++) {
        gets(st);
        len=strlen(st);
        for(int j=0;j<len/2;j++) {
            ch=st[j];
            st[j]=st[len-1-j];
            st[len-1-j]=ch;
        }
        printf("%s\n",st);
    }
    return 0;
}