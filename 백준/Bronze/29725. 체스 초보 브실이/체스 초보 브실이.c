#include <stdio.h>
struct code {
    char ch;
    int n;
};
int main(void) {
    char ps[9];
    int arr[2]={0,0};
    struct code rlt[6]={{'k',0},{'p',1},{'n',3},{'b',3},{'r',5},{'q',9}};
    for(int i=0;i<8;i++) {
        scanf("%s",ps);
        for(int j=0;j<8;j++) {
            if(ps[j]=='.')
                continue;
            else {
                for(int k=0;k<6;k++) {
                    if(ps[j]>=97 && rlt[k].ch==ps[j]) {
                        arr[1]+=rlt[k].n;
                        break;
                    } else if(ps[j]>=65 && rlt[k].ch==ps[j]+32) {
                        arr[0]+=rlt[k].n;
                        break;
                    }
                }
            }
        }
    }
    printf("%d",arr[0]-arr[1]);
    return 0;
}