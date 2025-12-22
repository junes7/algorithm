#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    int n;
    scanf("%d",&n);
    char *st=(char*)malloc(sizeof(char)*(n*5+1));
    for(int i=0;i<5;i++) {
        for(int j=0;j<n;j++) {
            memset(st,0,sizeof(char)*(n*5+1));
            if(i%2==0)
                for(int k=0;k<5*n;k++)
                    strcat(st,"@");
            else
                for(int k=0;k<n;k++)
                    strcat(st,"@");
            strcat(st,"\n");
            printf("%s",st);
        }
    }
    return 0;
}