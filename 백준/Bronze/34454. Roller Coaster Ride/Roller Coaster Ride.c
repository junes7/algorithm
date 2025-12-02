#include <stdio.h>
int main(void) {
    int n,c,p;
    scanf("%d %d %d",&n,&c,&p);
    printf("%s",n>c*p?"no":"yes");
    return 0;
}