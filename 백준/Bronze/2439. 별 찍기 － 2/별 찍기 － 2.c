#include <stdio.h>

int main(void) {
    int n;
    scanf("%d",&n);
    
    for(int i=1;i<n+1;i++) {
        for(int j=0;j<n-i;j++)
            printf(" ");
        for(int j=0;j<i;j++)
            printf("*");
        printf("\n");
    }
    return 0;
}