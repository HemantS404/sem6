def matBuild(key):
    alpha = [chr(i + ord("A")) if i != (ord("I") - ord("A")) else "IJ" for i in range(26)]
    alpha.remove("J")
    mat = []
    for i in range(5):
        matx = []
        for j in range(5):
            if len(key) != 0:
                ele = key[0]
                if ele != "I" and ele != "J":
                    matx.append(ele)
                    key = key.replace(ele, "")
                    alpha.remove(ele)
                else:
                    matx.append("IJ")
                    key = key.replace("I", "")
                    key = key.replace("J", "")
                    alpha.remove("I")
                    alpha.remove("J")
            else:
                ele = alpha[0]
                matx.append(ele)
                alpha.pop(0)
        mat.append(matx)

    return mat

def textpreprocess(text):
    textsplit = []
    i = 0
    while i < len(text) - 1:
        t = text[i]
        t1 = text[i+1]
        if t != t1:
            textsplit.append(t+t1)
            i+=2
        else:
            textsplit.append(t+verbose)
            i+=1

    return textsplit

def find(letter, mat):
    for i in range(5):
        for j in range(5):
            if letter == mat[i][j]:
                return i, j
    else:
        return find('IJ')

text = "GREET".upper()
key = "MOON".upper()
print(f"Plain Text : {text}")
print(f"Key : {key}")

verbose = 'X'.upper()
mat = matBuild(key)

textsplit = textpreprocess(text)
ciphersplit = []
for i in textsplit:
    i1, j1 = find(i[0], mat)
    i2, j2 = find(i[1], mat)
    if i1 == i2:
        j1 = (j1+1)%5
        j2 = (j2+1)%5
    elif j1 == j2:
        i1 = (i1+1)%5
        i2 = (i2+1)%5
    else:
        j1, j2 = j2, j1
    
    ciphersplit.append(mat[i1][j1] + mat[i2][j2])

cipher = ""
for i in ciphersplit:
    cipher+=i
print(f"Cipher Text : {cipher}")

ciphersplit = [cipher[i]+cipher[i+1] for i in range(0, len(cipher), 2)]
deciphersplit = []
for i in ciphersplit:
    i1, j1 = find(i[0], mat)
    i2, j2 = find(i[1], mat)
    if i1 == i2:
        j1 = (j1 - 1)%5
        j2 = (j2 - 1)%5
    elif j1 == j2:
        i1 = (i1 - 1)%5
        i2 = (i2 - 1)%5
    else:
        j1, j2 = j2, j1
    deciphersplit.append(mat[i1][j1] + mat[i2][j2])

decipher = ""
for i in deciphersplit:
    decipher += i
decipher = decipher.replace(verbose, "")
print(f"Deciphet Text : {decipher}")