#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    char *a=(char*)malloc(sizeof(char)*21);
    char *b=(char*)malloc(sizeof(char)*21);
    scanf("%s %s",a,b);
    printf("%d",strcmp(a,b)!=0?1550:0);
    return 0;
}