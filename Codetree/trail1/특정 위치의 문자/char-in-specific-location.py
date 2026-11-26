arr=['L','E','B','R','O','S']
idx,ch=-1,input()
for i,chr in enumerate(arr):
    if chr==ch:
        idx=i
print("None" if idx==-1 else idx)