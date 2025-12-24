#include <stdio.h>
#include <stdlib.h>
int main(void) {
    int k,n,m,cnt=0,*a,*b;
    scanf("%d %d",&k,&n);
    a=(int*)malloc(sizeof(int)*n);
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
    scanf("%d",&m);
    b=(int*)malloc(sizeof(int)*m);
    for(int i=0;i<m;i++)
        scanf("%d",&b[i]);
    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            if(a[i]+k==b[j])
                cnt+=1;
        }
    }
    printf("%d",cnt);
    return 0;
}