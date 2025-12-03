#include <stdio.h>
#include <stdbool.h>
int main(void) {
    int n,elem;
    bool rlt=true;
    scanf("%d",&n);
    for(int i=0;i<n;i++) {
        scanf("%d",&elem);
        if(elem<48) {
            rlt=false;
            break;
        }
    }
    printf("%s",rlt?"True":"False");
    return 0;
}