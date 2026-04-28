#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char** solution(const char* myStr) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    // r[0]="EMPTY";
    char* myStrCpy=(char*)malloc(sizeof(char)*strlen(myStr));
    char* temp=(char*)malloc(sizeof(char)*strlen(myStr));
    memset(temp,0,sizeof(char)*strlen(myStr));
    strcpy(myStrCpy,myStr);
    int start=-1,end=-1,idx=0,idx2=0;
    for(int i=0;i<strlen(myStrCpy);i++) {
        if(myStrCpy[i]=='a' || myStrCpy[i]=='b' || myStrCpy[i]=='c')
            myStrCpy[i]=32;
    }
    char** r=(char**)malloc(sizeof(char*)*(strlen(myStr)+1));
    strcat(myStrCpy," ");
    for(int i=0;i<strlen(myStrCpy);) {
        if(isalpha(myStrCpy[i])) {
            // printf("%c %d ",myStrCpy[i],start);
            if(start==-1)
                start=i;
            temp[idx++]=myStrCpy[i];
            i++;
        } else {
            if(isalpha(myStrCpy[i-1])) {
                end=i-1;
                temp[idx]='\0';
                // printf("temp: %s\n",temp);
                // printf("end-start+1: %d\n",end-start+1);
                r[idx2]=(char*)malloc(sizeof(char)*(end-start+1)+1);
                strcpy(r[idx2],temp);
                idx2++;
                idx=0,start=-1;
                memset(temp,0,sizeof(char)*strlen(myStr));
            }
            i++;
        }
    }
    if(idx2==0)
        r[0]="EMPTY";
    return r;
}