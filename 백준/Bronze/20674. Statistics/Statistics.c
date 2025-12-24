#include <stdio.h>
int main(void) {
    int n,prev=1000,rlt=0,tmp;
    scanf("%d",&n);
    for(int i=0;i<n;i++) {
        scanf("%d",&tmp);
        if(prev>=tmp)
            prev=tmp;
        else
            rlt+=tmp-prev;
    }
    printf("%d",rlt);
    return 0;
}