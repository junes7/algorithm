#include <stdio.h>
int main(void) {
    int d,e,q;
    char op;
    scanf("%d %d",&d,&e);
    for(int i=0;i<e;i++) {
        getchar();
        scanf("%c %d",&op,&q);
        d=op=='+'?d+q:d-q;
    }
    printf("%d",d);
    return 0;
}