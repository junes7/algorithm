#include <stdio.h>
struct cl {
    char ch;
    char word[12];
};
int main(void) {
    char st[9];
    scanf("%s",st);
    struct cl rlt[4]={{'F',"Foundation"},
    {'C',"Claves"},{'V',"Veritas"},{'E',"Exploration"}};
    for(int i=0;i<4;i++) {
        if(rlt[i].ch==st[0]) {
            printf("%s",rlt[i].word);
            break;
        }
    }
    return 0;
}