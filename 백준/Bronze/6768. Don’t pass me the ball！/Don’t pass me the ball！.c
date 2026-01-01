#include <stdio.h>
int main(void) {
    int j;
    scanf("%d", &j);
    printf("%d", (j - 1) * (j - 2) * (j - 3) / 6);
    return 0;
}