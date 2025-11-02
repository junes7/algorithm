import sys
input=lambda:sys.stdin.readline().rstrip()
n=int(input())
arr=[]
length=0 #앵무새가 말한 단어의 총 개수
for i in range(n):
    arr.append(input().split())
    length+=len(arr[i])
    arr[i].append(0)
res=input().split() #정답 문장
for word in res:
    isOk=0 #단어가 있어서 pop하면 1로 바꿀것임
    for i in range(n):
        if arr[i][0]==word:
            arr[i].pop(0)
            isOk=1
            break
    if isOk==0:
        break
if isOk==0 or length!=len(res):
    print("Impossible")
elif isOk==1 and length==len(res):
    print("Possible")