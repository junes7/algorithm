#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* s) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* r= (char*)malloc(sizeof(char)*strlen(s));
    int med=strlen(s)/2,idx=0;
    if(strlen(s)%2==0)
        r[idx++]=s[med-1];
    r[idx++]=s[med];
    r[idx]='\0';
    return r;
}