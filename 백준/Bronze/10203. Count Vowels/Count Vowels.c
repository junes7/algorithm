#include <stdio.h>
#include <string.h>
int main(void) {
    int n, cnt;
    char st[100], vowel[5] = {'a', 'e', 'i', 'o', 'u'};
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        cnt = 0;
        scanf("%s", st);
        for (int j = 0; j < strlen(st); j++) {
            for (int k = 0; k < 5; k++) {
                if (st[j] == vowel[k]) {
                    cnt += 1;
                    break;
                }
            }
        }
        printf("The number of vowels in %s is %d.\n", st, cnt);
    }
    return 0;
}