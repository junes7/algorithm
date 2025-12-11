#include <stdio.h>
int main(void) {
    int w1,h1,w2,h2;
    scanf("%d %d %d %d",&w1,&h1,&w2,&h2);
    printf("%d",4+(w1>w2?w1:w2)*2+(h1+h2)*2);
    return 0;
}