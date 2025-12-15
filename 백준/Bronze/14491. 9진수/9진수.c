#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char* solve(char r[],int n) {
    if(n==0)
        return r;
    char *tmp=(char*)malloc(sizeof(char)*6);
    if(n%9)
        sprintf(tmp,"%d",n%9);    
    else
        strcat(tmp,"0");
    strcat(tmp,r);
    return solve(tmp,n/9);
}
int main(void) {
    int n;
    scanf("%d",&n);
    printf("%s",solve("",n));
    return 0;
}