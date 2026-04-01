#include <stdio.h>
int main(void) {
    int n;
    long long a = 1, b = 1, t;
    scanf("%d", &n);
    for (int i = 0; i < n - 1; i++) {
        t = a;
        a = b;
        b = b + t;
    }
    printf("%lld", (a + b) * 2);
    return 0;
}