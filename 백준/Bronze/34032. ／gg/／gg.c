#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    int n, mid, cnt = 0;
    char* st = (char*)malloc(sizeof(char) * 500001);
    scanf("%d %s", &n, st);
    mid = n / 2 + (n % 2 == 0 ? 0 : 1);
    for (int i = 0; i < strlen(st); i++) {
        if (st[i] == 'O')
            cnt += 1;
    }
    printf("%s", cnt >= mid ? "Yes" : "No");
    return 0;
}