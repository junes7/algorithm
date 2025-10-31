import sys
input=lambda:sys.stdin.readline().rstrip()
n = int(input())
nums = list(map(int, input().split()))
ans = 0
ires = 1
for i in range(0, n-3):
    ires *= nums[i]
    jres = 1
    for j in range(i+1, n-2):
        jres *= nums[j]
        kres = 1
        for k in range(j+1, n-1):
            kres *= nums[k]
            lres = 1
            for l in range(k+1, n):
                lres *= nums[l]
            ans = max(ans, ires+jres+kres+lres)
print(ans)