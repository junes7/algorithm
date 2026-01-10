#include <math.h>
#include <stdio.h>
int main(void) {
    int t, n;
    double tmp;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        scanf("%d", &n);
        tmp = sqrt(n);
        printf("%d\n", tmp == (int)tmp ? 1 : 0);
    }
    return 0;
}