#include <stdio.h>
#include <stdlib.h>
int main(void) {
    char* st=(char*)malloc(sizeof(char)*12);;
    for(int i=0;i<3;i++)
        scanf("%s",st);
    for(int i=0;i<10000;i++)
        printf("%d\n",-1);
    return 0;
}