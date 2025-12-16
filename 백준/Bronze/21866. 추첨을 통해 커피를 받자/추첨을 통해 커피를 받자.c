#include <stdio.h>
int main(void) {
    int hac=0,total=0,arr[9],maxn[]={100,100,200,200,300,300,400,400,500};
    for(int i=0;i<9;i++) {
        scanf("%d",&arr[i]);
        if(arr[i]>maxn[i]) {
            hac=1;
            break;
        }
        total+=arr[i];
    }
    printf("%s",hac?"hacker":(total>=100?"draw":"none"));
    return 0;
}