#include <stdio.h>
#include <string.h>
int main(void) {
    int a,b;
    char c[101];
    scanf("%d %d %s",&a,&b,c);
    if((c[strlen(c)-1]-48)%2)
        printf("%d",a^b);
    else
        printf("%d",a);
    return 0;
}