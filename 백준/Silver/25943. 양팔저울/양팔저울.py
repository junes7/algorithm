import sys
input=lambda:sys.stdin.readline().rstrip()
n = int(input())
gravel_list = list(map(int, input().split()))
weight_list=  [100, 50, 20, 10, 5, 2, 1]
left = gravel_list[0]
right = gravel_list[1]
for i in gravel_list[2:]:
    if left == right:
        left += i
        continue
    if left < right:
        left += i
    elif right < left:
        right += i
if left == right:
    print(0)
else:
    difference = max(left, right) - min(left, right)
    count = 0
    for weight in weight_list:   
        if difference < weight:
            continue      
        count += difference // weight
        difference %= weight
    print(count)