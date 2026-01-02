#include <math.h>
#include <stdio.h>
#include <stdlib.h>
struct col {
    char ch;
    double rate;
};
int main(void) {
    int n;
    double ori;
    char dot, vou, pri;
    struct col dic[6] = {{'R', 0.55}, {'G', 0.7}, {'B', 0.8}, {'Y', 0.85}, {'O', 0.9}, {'W', 0.95}};
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lf %c %c %c", &ori, &dot, &vou, &pri);
        for (int j = 0; j < 6; j++) {
            if (dic[j].ch == dot) {
                ori *= dic[j].rate;
                break;
            }
        }
        if (vou == 'C')
            ori *= 0.95;
        ori *= 100;
        if (pri == 'C') {
            if (fmod(ori, 10) > 5) ori += 10;
            ori -= fmod(ori, 10);
        }
        printf("$%.2f\n", ori / 100);
    }
    return 0;
}