#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arr_len은 배열 arr의 길이입니다.
// delete_list_len은 배열 delete_list의 길이입니다.
int* solution(int arr[], size_t arr_len, int delete_list[], size_t delete_list_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* r=(int*)malloc(sizeof(int)*arr_len);
    int cnt=0;
    bool flag;
    for(int i=0;i<arr_len;i++) {
        flag=true;
        for(int j=0;j<delete_list_len;j++) {
            if(delete_list[j]==arr[i]) {
                flag=false;
                break;
            }
        }
        if(flag)
            r[cnt++]=arr[i];
    }
    return r;
}