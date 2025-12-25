#include <stdio.h>
#include <stdlib.h>
int main(void) {
    int n,yr;
    char *sub = (char*)malloc(sizeof(char)*16);
    scanf("%d",&n);
    for(int i=0;i<n;i++) {
        scanf("%s %d",sub,&yr);
        if(yr==2026) {
            printf("%s",sub);
            break;
        }
    }
    return 0;
}