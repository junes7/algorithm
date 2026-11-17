tot,cnt=0,0
while True:
    n=int(input())
    if n<20 or n>29:
        print(f"{tot/cnt:.2f}")
        break
    tot+=n
    cnt+=1