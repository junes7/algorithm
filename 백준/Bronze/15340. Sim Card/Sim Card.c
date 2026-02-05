#include <stdbool.h>
#include <stdio.h>
int main(void) {
    int c, d, rlt, tmp, comp[3][2] = {{30, 40}, {35, 30}, {40, 20}};
    while (true) {
        scanf("%d %d", &c, &d);
        if (c == 0 && d == 0) break;
        rlt = 100000;
        for (int i = 0; i < 3; i++) {
            tmp = comp[i][0] * c + comp[i][1] * d;
            if (rlt > tmp) rlt = tmp;
        }
        printf("%d\n", rlt);
    }
    return 0;
}