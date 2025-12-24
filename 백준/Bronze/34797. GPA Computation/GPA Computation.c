#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct gr{
    char ch;
    int num;
};
int main(void) {
    int n,rlt=0;
    double bn=0;
    char tar[]="ABC",*st=(char*)malloc(sizeof(char)*3);
    struct gr grade[5]={{'A',4},{'B',3},{'C',2},{'D',1},{'E',0}};
    scanf("%d",&n);
    for(int i=0;i<n;i++) {
        scanf("%s",st);
        for(int j=0;j<5;j++) {
            if(grade[j].ch==st[0]) {
                if(strchr(tar,st[0])!=NULL) {
                    if(st[1]=='1')
                        bn+=0.05;
                    else if(st[1]=='2')
                        bn+=0.025;
                }
                rlt+=grade[j].num;
                break;
            }
        }
    }
    printf("%.6lf",(double)rlt/n+bn);
    return 0;
}