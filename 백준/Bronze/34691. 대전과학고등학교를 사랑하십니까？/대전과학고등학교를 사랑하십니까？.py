import sys
input=lambda:sys.stdin.readline().rstrip()
while True:
    word=input()
    if word=="end": break
    if word=="animal":
        print("Panthera tigris")
    elif word=="tree":
        print("Pinus densiflora")
    elif word=="flower":
        print("Forsythia koreana")