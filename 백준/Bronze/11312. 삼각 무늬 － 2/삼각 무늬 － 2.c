#include <stdio.h>
int main(void) {
    int t;
    long a, b;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        scanf("%ld %ld", &a, &b);
        printf("%ld\n", (a / b) * (a / b));
    }
    return 0;
}