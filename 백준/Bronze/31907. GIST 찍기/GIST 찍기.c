#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    int n,idx;
    scanf("%d", &n);
    char p_list[3][5]={"G...",".I.T","..S."};
    char *str=(char*)malloc(sizeof(char)*(4*n+1));
    for(int i=0;i<sizeof(p_list)/5;i++) {
        idx=0;
        for(int j=0;j<strlen(p_list[i]);j++) {
            for(int k=0;k<n;k++) {
                str[idx++]=p_list[i][j];
            }
        }
        str[idx]='\0';
        for(int j=0;j<n;j++) {
            printf("%s\n",str);
        }
    }
    return 0;
}