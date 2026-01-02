#include <stdio.h>
int main(void) {
    int n, x;
    scanf("%d %d", &n, &x);
    double tmp = n * (1 - x / 100.0);
    printf("%.6f", (n / tmp - 1) * 100);
    return 0;
}