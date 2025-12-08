#include <stdio.h>
int main(void) {
    int y,c,p,tmp;
    scanf("%d %d %d",&y,&c,&p);
    tmp=y<c/2?y:c/2;
    tmp=tmp>p?p:tmp;
    printf("%d",tmp);
    return 0;
}