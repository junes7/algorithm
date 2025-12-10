#include <stdio.h>
int main(void) {
    int s;
    double d,t;
    scanf("%d %lf %lf",&s,&d,&t);
    printf("%s",d/(s*5280/3600)<=t?"MADE IT":"FAILED TEST");
    return 0;
}