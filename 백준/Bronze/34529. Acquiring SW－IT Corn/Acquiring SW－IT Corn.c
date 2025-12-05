#include <stdio.h>
int main(void) {
    int total=0,price[3],plan[3];
    int unit[3]={100,50,20};
    for(int i=0;i<3;i++)
        scanf("%d",&price[i]);
    for(int i=0;i<3;i++)
        scanf("%d",&plan[i]);
    for(int i=0;i<3;i++)
        total+=plan[i]/unit[i]*price[i];
    printf("%d",total);
    return 0;
}