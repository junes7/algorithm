#include <stdio.h>
void swap(int *p,int *q) {
    int tmp;
    tmp=*p;
    *p=*q;
    *q=tmp;
}
int main(void) {
    int a,b,c,d,s,e,mid,fit,rlt;
    while(1) {
        scanf("%d %d %d %d",&a,&b,&c,&d);
        if(a==0 && b==0 && c==0 && d==0) break;
        if(a<b) swap(&a,&b);
        if(c<d) swap(&c,&d);
        s=1,e=100;
        while(s<=e) {
            mid=(s+e)/2;
            fit=(a*mid>c*100||b*mid>d*100)?0:1;
            if(fit) {
                s=mid+1;
                rlt=mid;
            } else {
                e=mid-1;
            }
        }
        printf("%d%%\n",rlt);
    }
    return 0;
}