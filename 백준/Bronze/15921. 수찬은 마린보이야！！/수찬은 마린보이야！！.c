#include <stdio.h>
int main(void) {
    int n,sumn;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++) {
        scanf("%d",&arr[i]);
        sumn+=arr[i];
    }
    if(n==0)
        printf("%s","divide by zero");
    else
        printf("%.2lf",(double)sumn/n/(sumn/n));
    return 0;
}