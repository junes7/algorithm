import sys
input=lambda:sys.stdin.readline().rstrip()
consonant = 'b k x z n h d c w g p v j q t s r l m f'.split()
vowel = 'a i y e o u'.split()
lines = sys.stdin.readlines()
for line in lines:
    ciphertext = line.rstrip()
    plaintext = ''
    for char in ciphertext:
        if not char.isalpha():
            plaintext += char
            continue
        is_upper = False
        if char.isupper():
            is_upper = True
        temp = ''
        if char.lower() in vowel:
            index = vowel.index(char.lower())
            temp = vowel[(index + 3) % len(vowel)]
        else:
            index = consonant.index(char.lower())
            temp = consonant[(index + 10) % len(consonant)]
        plaintext += temp.upper() if is_upper else temp
    print(plaintext)