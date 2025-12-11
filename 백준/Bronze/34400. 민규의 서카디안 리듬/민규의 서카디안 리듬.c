#include <stdio.h>
int main(void) {
    int n,t;
    scanf("%d",&n);
    for(int i=0;i<n;i++) {
        scanf("%d",&t);
        printf("%s\n",t%25<17?"ONLINE":"OFFLINE");
    }
    return 0;
}