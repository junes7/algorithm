def fact(n) : 
    if n == 1 or n == 0 : 
        return 1
    return n * fact(n-1)
N = int(input())
print(fact(N) // (fact(N-5) * fact(5)))