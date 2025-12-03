#include <stdio.h>
int main(void) {
    int m,d;
    scanf("%d %d",&m,&d);
    printf("%d",d/m+(d%m==0?0:1));
    return 0;
}