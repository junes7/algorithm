#include <stdio.h>
int main(void) {
    long n,m,s;
    scanf("%ld %ld %ld",&n,&m,&s);
    printf("%ld",s*m<s*(m+1)*(100-n)/100?s*m:s*(m+1)*(100-n)/100);
    return 0;
}