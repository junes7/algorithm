gd = int(input())
age = int(input())
if gd == 0:
    print("MAN" if age >= 19 else "BOY")
elif gd == 1:
    print("WOMAN" if age >= 19 else "GIRL")