#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    char *word=(char*)malloc(sizeof(char)*7);
    while(scanf("%s",word)) {
        if(strcmp(word,"end")==0) break;
        if(strcmp(word,"animal")==0) {
            printf("Panthera tigris\n");
        } else if(strcmp(word,"tree")==0) {
            printf("Pinus densiflora\n");
        } else if(strcmp(word,"flower")==0) {
            printf("Forsythia koreana\n");
        }
    }
    return 0;
}