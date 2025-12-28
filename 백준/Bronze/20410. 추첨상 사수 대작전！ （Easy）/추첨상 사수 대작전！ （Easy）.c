#include <stdio.h>
int main(void) {
    int m,seed,x1,x2,a,c;
    scanf("%d %d %d %d",&m,&seed,&x1,&x2);
    for(int a=0;a<m;a++) {
        for(int c=0;c<m;c++) {
            if(x1==(a*seed+c)%m && x2==(a*x1+c)%m) {
                printf("%d %d",a,c);
                return 0;
            }
        }
    }
}