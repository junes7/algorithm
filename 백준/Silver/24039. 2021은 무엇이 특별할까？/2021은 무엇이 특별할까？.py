import math
n = int(input())
is_prime_num = [True for i in range(n+1)]
prime_num = []
start = 0
if n<4:
    print(6)
else:
		# 에라토스테네의 체 알고리즘
    for i in range(2, int(math.sqrt(n))+1):
        j = 2
        while i*j <= n:
            is_prime_num[i*j] = False
            j+=1        
    for i in range(2, n+1):
        if is_prime_num[i] == True:
            prime_num.append(i)
            if i <= int(math.sqrt(n)):
                start = i 
		# 답 찾기 (for문은 한 번 아니면 두번 돌고 나온다.)
    for i in range(prime_num.index(start), len(prime_num)-1):
        result = prime_num[i] * prime_num[i+1]
        if result > n:
            print(result)
            break