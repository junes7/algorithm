#include <stdio.h>
#include <math.h>
int main(void) {
    int a,b,n;
    while(1) {
        scanf("%d %d",&b,&n);
        if(b==0 && n==0) break;
        a=1;
        while(pow(a,n)<b)
            a+=1;
        printf("%d\n",pow(a,n)-b<b-pow(a-1,n)?a:a-1);
    }
    return 0;
}