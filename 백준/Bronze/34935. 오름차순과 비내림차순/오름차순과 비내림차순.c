#include <stdio.h>
#include <stdbool.h>
int main(void) {
    int n;
    bool rlt=true;
    scanf("%d",&n);
    long long arr[n];
    scanf("%lld",&arr[0]);
    for(int i=1;i<n;i++) {
        scanf("%lld",&arr[i]);
        if(arr[i-1]>=arr[i]) {
            rlt=false;
            break;
        }
    }
    printf("%d",rlt?1:0);
    return 0;
}