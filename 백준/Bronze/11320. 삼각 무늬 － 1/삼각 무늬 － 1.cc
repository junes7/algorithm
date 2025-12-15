#include <stdio.h>
#include <math.h>
int main(void) {
    int t,a,b;
    scanf("%d",&t);
    for(int i=0;i<t;i++) {
        scanf("%d %d",&a,&b);
        printf("%d\n",(int)pow(a/b,2));
    }
    return 0;
}