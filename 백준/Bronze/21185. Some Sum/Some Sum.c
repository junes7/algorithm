#include <stdio.h>
int main(void) {
    int n;
    scanf("%d",&n);
    printf("%s",n%4==0?"Even":(n%2==0?"Odd":"Either"));
    return 0;
}