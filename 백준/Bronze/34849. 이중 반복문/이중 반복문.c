#include <stdio.h>
#include <math.h>
int main(void) {
    long n;
    scanf("%ld",&n);
    printf(n*n/pow(10,8)>1?"Time limit exceeded":"Accepted");
    return 0;
}