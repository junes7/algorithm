#include <stdio.h>
int main(void) {
    int n,rlt=0;
    scanf("%d",&n);
    for(int i=1;i<n+1;i++) {
        if(n%i==0)
            rlt+=i;
    }
    printf("%d",rlt*5-24);
    return 0;
}