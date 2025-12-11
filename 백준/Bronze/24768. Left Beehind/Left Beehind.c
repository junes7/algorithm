#include <stdio.h>
int main(void) {
    int x,y;
    while(1) {
        scanf("%d %d",&x,&y);
        if(x==0 && y==0) break;
        if(x+y==13)
            printf("%s\n","Never speak again.");
        else {
            if(x>y) printf("%s\n","To the convention.");
            else if(x<y) printf("%s\n","Left beehind.");
            else printf("%s\n","Undecided.");
        }
    }
    return 0;
}