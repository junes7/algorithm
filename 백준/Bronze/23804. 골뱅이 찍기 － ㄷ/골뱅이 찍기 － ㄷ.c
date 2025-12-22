#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    int n;
    scanf("%d",&n);
    char *st=(char*)malloc(sizeof(char)*(n*5+1));
    for(int i=0;i<n*5;i++) {
    memset(st,0,sizeof(char)*(n*5+1));
        if(i<n || i>=n*5-n)
            for(int j=0;j<n*5;j++)
                strcat(st,"@");
        else
            for(int j=0;j<n;j++)
                strcat(st,"@");
        strcat(st,"\n");
        printf("%s",st);
    }
    return 0;
}