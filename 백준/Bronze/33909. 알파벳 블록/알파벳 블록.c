#include <stdio.h>
#include <stdlib.h>
int main(void) {
    int* arr = (int*)malloc(sizeof(int) * 4);
    for (int i = 0; i < 4; i++)
        scanf("%d", &arr[i]);
    arr[0] += arr[3];
    arr[1] += arr[2] * 2;
    printf("%d", arr[0] / 3 < arr[1] / 6 ? arr[0] / 3 : arr[1] / 6);
    return 0;
}