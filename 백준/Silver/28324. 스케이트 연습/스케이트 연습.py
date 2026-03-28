num = int(input()) #입력 개수
vel = list(map(int,input().split())) #속력 제한
count = 1
result = 0
for i in range(num-1,-1,-1):
    if count <= vel[i]:
        result += count
        #print(f'count 더함 result:{result}')
        count += 1
    else:
        result += vel[i]
        #print(f'vel 더함 result:{result}')
        count = vel[i] + 1     
print(result)