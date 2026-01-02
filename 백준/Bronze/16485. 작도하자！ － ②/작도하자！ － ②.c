#include <stdio.h>
int main(void) {
    int c, b;
    scanf("%d %d", &c, &b);
    if (c % b == 0)
        printf("%d", c / b);
    else
        printf("%.6f", (double)c / b);
    return 0;
}