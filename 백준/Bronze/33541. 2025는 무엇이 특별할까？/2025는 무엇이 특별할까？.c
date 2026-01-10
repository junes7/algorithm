#include <math.h>
#include <stdbool.h>
#include <stdio.h>
int main(void) {
    int st, n1, n2;
    scanf("%d", &st);
    while (true) {
        n1 = st / 100, n2 = st % 100 + 1;
        st += 1;
        if (st > 9999) {
            printf("%d", -1);
            break;
        }
        if (st == pow(n1 + n2, 2)) {
            printf("%d", st);
            break;
        }
    }
    return 0;
}