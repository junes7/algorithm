h,m=map(int,input().split())
tot=h*60+m
if (6*60+30<=tot<=9*60
or 9*60+50<=tot<=10*60
or 10*60+50<=tot<=11*60
or 11*60+50<=tot<=12*60
or 12*60+50<=tot<=13*60+50
or 14*60+40<=tot<=14*60+50
or 15*60+40<=tot<=15*60+50
or 16*60+40<=tot<=22*60+50):
    print("Yes")
else:
    print("No")