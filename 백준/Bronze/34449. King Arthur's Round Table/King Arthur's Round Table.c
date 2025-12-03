#include <stdio.h>
int main(void) {
    double d,w;
    int n;
    scanf("%lf %lf %d",&d,&w,&n);
    printf("%s",n<=d/w*3.14159?"YES":"NO");
    return 0;
}