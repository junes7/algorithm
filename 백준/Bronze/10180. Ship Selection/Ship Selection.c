#include <stdio.h>
int main(void) {
    int t,n,d,v,f,c,cnt;
    scanf("%d",&t);
    for(int i=0;i<t;i++) {
        scanf("%d %d",&n,&d);
        cnt=0;
        for(int j=0;j<n;j++) {
            scanf("%d %d %d",&v,&f,&c);
            if(v*f/c>=d)
                cnt+=1;
        }
        printf("%d\n",cnt);
    }
    return 0;
}