#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    int n;
    scanf("%d",&n);
    char **st=(char**)malloc(sizeof(char*)*(n*5));
    for(int i=0;i<n*5;i++) {
        st[i]=(char*)malloc(sizeof(char)*(n*5+1));
        memset(st[i],0,sizeof(char)*(n*5+1));
        if(i<n) {
            for(int j=0;j<n*3;j++)
                strcat(st[i],"@");
            for(int j=0;j<n;j++)
                strcat(st[i]," ");
            for(int j=0;j<n;j++)
                strcat(st[i],"@");
        } else if(n<=i && i<n*5-n) {
            for(int j=0;j<5;j++) {
                for(int k=0;k<n;k++)
                    strcat(st[i],j%2==0?"@":" ");
            }
        } else {
            for(int j=0;j<n;j++)
                strcat(st[i],"@");
            for(int j=0;j<n;j++)
                strcat(st[i]," ");
            for(int j=0;j<n*3;j++)
                strcat(st[i],"@");
        }
    }
    for(int i=0;i<n*5;i++)
        printf("%s\n",st[i]);
    return 0;
}