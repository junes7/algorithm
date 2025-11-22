n, k = map(int, input().split())
course = list(map(int, input().split()))
total = sum(course)
 
if k < total:
    tmp = 0
    for i in range(n):
        if tmp == k:
            print(i+1)
            break
        elif tmp > k:
            print(i)
            break
        tmp += course[i]
else:
    k -= total
    tmp = 0
    for i in range(n-1, -1, -1):
        if tmp+course[i] < k:
            tmp += course[i]
        else:
            print(i+1)
            break