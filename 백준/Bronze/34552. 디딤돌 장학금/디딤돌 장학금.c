#include <stdio.h>
int main(void) {
    int n,b,s,rlt=0,m[11];
    double l;
    for(int i=0;i<11;i++)
        scanf("%d",&m[i]);
    scanf("%d",&n);
    for(int i=0;i<n;i++) {
        scanf("%d %lf %d",&b,&l,&s);
        if(l>=2.0 && s>=17)
            rlt+=m[b];
    }
    printf("%d",rlt);
    return 0;
}