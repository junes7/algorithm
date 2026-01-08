#include <stdbool.h>
#include <stdio.h>
int main(void) {
    int n, rlt;
    while (true) {
        scanf("%d", &n);
        if (n == 0) break;
        rlt = 0;
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                rlt += i * j;
            }
        }
        printf("%d\n", rlt);
    }
    return 0;
}