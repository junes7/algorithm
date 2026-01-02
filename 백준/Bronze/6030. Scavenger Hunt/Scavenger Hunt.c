#include <stdio.h>
#include <stdlib.h>
int main(void) {
    int p, q, idxp = 0, idxq = 0;
    scanf("%d %d", &p, &q);
    int* pe = (int*)malloc(sizeof(int) * p);
    int* qe = (int*)malloc(sizeof(int) * q);
    for (int i = 1; i < p + 1; i++)
        if (p % i == 0)
            pe[idxp++] = i;
    for (int i = 1; i < q + 1; i++)
        if (q % i == 0)
            qe[idxq++] = i;
    for (int i = 0; i < idxp; i++) {
        for (int j = 0; j < idxq; j++)
            printf("%d %d\n", pe[i], qe[j]);
    }
    return 0;
}