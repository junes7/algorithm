#include <stdio.h>
#include <stdlib.h>
int main(void) {
    char *a=(char*)malloc(sizeof(char)*3);
    char *b=(char*)malloc(sizeof(char)*3);
    scanf("%s %s",a,b);
    int rlt[2]={abs(a[0]-b[0]),abs(a[1]-b[1])};
    printf("%d %d",rlt[0]>rlt[1]?rlt[1]:rlt[0],rlt[0]>rlt[1]?rlt[0]:rlt[1]);
    return 0;
}