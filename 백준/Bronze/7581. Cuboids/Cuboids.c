#include <stdio.h>
int main(void) {
    int l,w,h,v;
    while(1) {
        scanf("%d %d %d %d",&l,&w,&h,&v);
        if(l==0 && w==0 && h==0 && v==0) break;
        if(l==0)
            l=v/(w*h);
        else if(w==0)
            w=v/(l*h);
        else if(h==0)
            h=v/(l*w);
        else
            v=l*w*h;
        printf("%d %d %d %d\n",l,w,h,v);
    }
    return 0;
}