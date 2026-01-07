#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    int n, *arr;
    scanf("%d", &n);
    arr = (int*)malloc(sizeof(int) * n);
    memset(arr, 0, sizeof(int) * n);
    arr[0] = 1, arr[1] = 2, arr[n - 1] = 997;
    for (int i = 1; i < n; i++) {
        if (arr[i] == 0)
            arr[i] = arr[i - 1] + 1;
    }
    printf("%d\n", n);
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    return 0;
}