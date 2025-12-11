#include <stdio.h>
#include <string.h>
int main(void) {
    int t,n;
    char rlt[13];
    scanf("%d",&t);
    for(int i=0;i<t;i++) {
        scanf("%d",&n);
        strcpy(rlt,"Round 1");
        if(n<=25)
            strcpy(rlt,"World Finals");
        else if(n<=1000)
            strcpy(rlt,"Round 3");
        else if(n<=4500)
            strcpy(rlt,"Round 2");
        printf("Case #%d: %s\n",i+1,rlt);
    }
    return 0;
}