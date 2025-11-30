#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    int n;
    bool iskor=false;
    scanf("%d",&n);
    char **arr=(char**)malloc(sizeof(char*)*n);
    for(int i=0;i<n;i++) {
        arr[i]=(char*)malloc(sizeof(char)*51);
        scanf("%s",arr[i]);
        if(strcmp(arr[i],"korea")==0)
            iskor=true;
        if(strcmp(arr[i],"yonsei")==0) {
            printf("%s",iskor?"Yonsei Lost...":"Yonsei Won!");
            break;
        }
    }
    return 0;
}