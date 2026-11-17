a=["John","Tom","Paul","Sam"]
while True:
    n=int(input())
    if n>4:
        print("Vacancy")
        break
    print(a[n-1])