#include <stdio.h>
int main(void) {
    int n,m;
    scanf("%d %d",&n,&m);
    for(int i=0;i<n;i++) {
        for(int j=1;j<m+1;j++) {
            printf("%d",i*m+j);
            if(j!=m) printf(" ");
        }
        printf("\n");
    }
    return 0;
}