#include <stdio.h>
int main(void) {
    int n,prev,cur,rlt=1;
    scanf("%d %d",&n,&prev);
    for(int i=1;i<n;i++) {
        scanf("%d",&cur);
        if(prev<=cur) rlt+=1;
        prev=cur;
    }
    printf("%d",rlt);
    return 0;
}