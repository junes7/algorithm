import sys
input=lambda:sys.stdin.readline().rstrip()
input_str = input()
if input_str[0] == '_' or input_str[0].isupper() or input_str[-1] == '_':
    print("Error!")
    exit()
if input_str.count('_') > 0:    # C++ => Java
    new_str = ''
    underbar = False
    for i in range(len(input_str)):
        if input_str[i].isupper():
            new_str = "Error!"
            break
        if input_str[i].isalpha():
            if underbar:
                new_str += input_str[i].upper()
                underbar = False
            else:
                new_str += input_str[i]
        elif not underbar and input_str[i] == '_':
            underbar = True
        else:
            new_str = "Error!"
            break
else:   # Java => C++
    new_str = ''
    for i in range(len(input_str)):
        if input_str[i].isupper():
            new_str += ('_'+input_str[i].lower())
        elif input_str[i].islower():
            new_str += input_str[i]
        else:
            new_str = "Error!"
            break
print(new_str)