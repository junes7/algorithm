#include <stdio.h>
#include <math.h>
int main(void) {
    int l;
    scanf("%d",&l);
    printf("%.9f",0.5*l*l*sin(120*M_PI/180));
    return 0;
}