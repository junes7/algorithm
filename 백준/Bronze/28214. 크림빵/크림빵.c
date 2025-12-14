#include <stdio.h>
int main(void) {
    int n,k,p,elem,cnt=0,rlt=0;
    scanf("%d %d %d",&n,&k,&p);
    for(int i=0;i<n;i++) {
        cnt=0;
        for(int j=k*i;j<k*(i+1);j++) {
            scanf("%d",&elem);
            if(elem==0) cnt+=1;
        }
        if(cnt<p) rlt+=1;
    }
    printf("%d",rlt);
    return 0;
}