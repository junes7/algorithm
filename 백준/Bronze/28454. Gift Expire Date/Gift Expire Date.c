#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    int cnt = 0, n, idx = 0;
    char *temp, *st = (char*)malloc(sizeof(char) * 11);
    scanf("%s %d", st, &n);
    int carr[3], arr[3];
    temp = strtok(st, "-");
    while (temp != NULL) {
        carr[idx++] = atoi(temp);
        temp = strtok(NULL, "-");
    }
    for (int i = 0; i < n; i++) {
        idx = 0;
        scanf("%s", st);
        temp = strtok(st, "-");
        while (temp != NULL) {
            arr[idx++] = atoi(temp);
            temp = strtok(NULL, "-");
        }
        if (arr[0] > carr[0]) {
            cnt += 1;
        } else if (arr[0] == carr[0]) {
            if (arr[1] > carr[1])
                cnt += 1;
            else if (arr[1] == carr[1] && arr[2] >= carr[2])
                cnt += 1;
        }
    }
    printf("%d", cnt);
    return 0;
}