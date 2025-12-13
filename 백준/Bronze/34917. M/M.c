#include <stdio.h>
#include <string.h>
int main(void) {
    int t,n;
    char st[51];
    scanf("%d",&t);
    for(int i=0;i<t;i++) {
        scanf("%d",&n);
        for(int j=0;j<n;j++) {
            strcpy(st,"");
            for(int k=0;k<n;k++) {
                if(k==0 || k==n-1)
                    strcat(st,"#");                
                else {
                    if(1<=j && j<=n/2) {
                        if(k==j || k==n-1-j)
                            strcat(st,"#");
                        else
                            strcat(st,".");
                    } else {
                        strcat(st,".");
                    }
                }
            }
            printf("%s\n",st);
        }
    }
}