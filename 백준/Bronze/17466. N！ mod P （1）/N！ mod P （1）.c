#include <stdio.h>
int main(void) {
    int n, p;
    long long rlt = 1;
    scanf("%d %d", &n, &p);
    for (int i = 2; i < n + 1; i++)
        rlt = rlt * i % p;
    printf("%lld", rlt);
    return 0;
}