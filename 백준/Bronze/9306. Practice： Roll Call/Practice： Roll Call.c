#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    char* name=(char*)malloc(sizeof(char)*20);
    int n;
    scanf("%d", &n);
    char** names=(char**)malloc(sizeof(char*)*(n*2));
    for(int i=0;i<n;i++) {
        names[2*i]=(char*)malloc(sizeof(char)*20);
        scanf("%s", name);
        strcpy(names[2*i], name);
        names[2*i+1]=(char*)malloc(sizeof(char)*20);
        scanf("%s", name);
        strcpy(names[2*i+1], name);
    }
    for(int i=0;i<n;i++) {
        printf("Case %d: %s, %s\n",i+1,names[2*i+1],names[2*i]);
    }
    return 0;
}