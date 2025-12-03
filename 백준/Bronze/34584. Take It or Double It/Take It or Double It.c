#include <stdio.h>
int main(void) {
    int x,d;
    scanf("%d %d",&x,&d);
    printf("%s",d/x<2?"take it":"double it");
    return 0;
}