cnt3,cnt5=0,0
for _ in range(10):
    el=int(input())
    if el%3==0:
        cnt3+=1
    if el%5==0:
        cnt5+=1
print(cnt3,cnt5)