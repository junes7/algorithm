#include <stdio.h>
#include <math.h>
int main(void) {
    int r,w,l,cnt=1;
    while(1) {
        scanf("%d",&r);
        if(r==0) break;
        scanf("%d %d",&w,&l);
        printf("Pizza %d %s on the table.\n",cnt++,2*r>=sqrt(w*w+l*l)?"fits":"does not fit");
    }
    return 0;
}