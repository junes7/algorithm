import sys
input = sys.stdin.readline
W, H, X, Y, P = map(int, input().split())
check_people = 0
for i in range(P):
    x, y = map(int, input().split()) 
    radius = H/2
    distance1 = ((x-X)**2 + (y-(Y+radius))**2)
    distance2 = ((x-(X+W))**2 + (y-(Y+radius))**2)
    radius_2 = radius*radius
    if (X+W) >= x and x >= X and y >= Y and y <= (Y+H): # 사각형
        check_people += 1
    elif distance1 <= radius_2 or distance2 <= radius_2: # 반원
        check_people += 1  
print(check_people)