#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    char* s = (char*)malloc(sizeof(char) * 101);
    char* t = (char*)malloc(sizeof(char) * 10001);
    char* rlt = (char*)malloc(sizeof(char) * 10000);
    bool exist;
    int idx = 0;
    scanf("%s %s", s, t);
    for (int i = 0; i < strlen(t); i++) {
        exist = false;
        for (int j = 0; j < strlen(s); j++) {
            if (s[j] == t[i]) {
                exist = true;
                break;
            }
        }
        if (!exist) {
            rlt[idx++] = t[i];
        }
    }
    rlt[idx] = '\0';
    printf("%s", rlt);
    return 0;
}