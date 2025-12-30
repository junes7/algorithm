#include <stdio.h>
#include <stdlib.h>
int main(void) {
    int n,rlt=0;
    char *a=(char*)malloc(sizeof(char)*100001);
    char *b=(char*)malloc(sizeof(char)*100001);
    scanf("%d %s %s",&n,a,b);
    for(int i=0;i<n;i++) {
        if(a[i]!=b[i])
            rlt+=1;
    }
    printf("%d",rlt);
    return 0;
}