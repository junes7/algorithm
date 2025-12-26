#include <stdio.h>
#include <stdlib.h>
int main(void) {
    char *a,*p;
    a=(char*)malloc(sizeof(char)*101);
    p=(char*)malloc(sizeof(char)*101);
    scanf("%s %s",a,p);
    printf("%s",p);
    return 0;
}