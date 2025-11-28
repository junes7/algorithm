#include <stdio.h>
int main(void) {
    int n,si,ci,ai,ri,cnt=0;
    scanf("%d",&n);
    for(int i=0;i<n;i++) {
        scanf("%d %d %d %d",&si,&ci,&ai,&ri);
        if(si>=1000 || ci>=1600 || ai>=1500 || (1<=ri&&ri<=30))
            cnt+=1;
    }
    printf("%d",cnt);
    return 0;
}