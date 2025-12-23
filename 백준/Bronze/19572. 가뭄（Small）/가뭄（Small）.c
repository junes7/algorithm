#include <stdio.h>
int main(void) {
    int d1,d2,d3;
    double sumn,a,b,c;
    scanf("%d %d %d",&d1,&d2,&d3);
    sumn=(d1+d2+d3)/2.0;
    a=sumn-d3;
    b=sumn-d2;
    c=sumn-d1;
    if(a>0 && b>0 &&c>0) {
        printf("%d\n%.1lf %.1lf %.1lf",1,a,b,c);
    } else
        printf("%d",-1);
    return 0;
}