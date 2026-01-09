import sys
input=lambda:sys.stdin.readline().rstrip("\n")
for _ in range(int(input())):
    st,vowel,cnt=input(),['a','e','i','o','u'],0
    for c in st:
        if c in vowel:
            cnt+=1
    print(f"The number of vowels in {st} is {cnt}.")