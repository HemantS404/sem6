import random

def ranker(key):
    rank = []
    for i in key:
        count = 0
        for j in key:
            if i > j:
                count += 1
        rank.append(count + 1)
    for i in range(len(rank)):
        c = 1
        for j in range(i+1,len(rank)):
            if rank[i] == rank[j]:
                rank[j] += c
                c += 1
    return rank

def matBuilder(text, key):
    mat = []

    extra = [chr(random.randint(0, 25) + ord("A")) for _ in range(len(key) - len(text)%len(key) if len(text)%len(key)!=0 else 0)]
    for i in extra:
        text += i
    i = 0
    while i<len(text):
        matx = []
        for _ in range(len(key)):
            matx.append(text[i])
            i+=1
        mat.append(matx)

    return mat

def matTrasposer(mat, rank):
    cipher = ""
    for i in range(1, len(rank) + 1):
        for j in range(len(rank)):
            if i == rank[j]:
                for k in range(len(mat)):
                    cipher += mat[k][j]
    return cipher

def reverseTrasposer(cipher, rank):
    mat = [["" for _ in range(len(rank))] for _ in range(len(cipher)//len(rank))]
    ciphersplit = []
    i = 0
    while i < len(cipher):
        ctext = ""
        for _ in range(len(cipher)// len(rank)):
            ctext += cipher[i]
            i += 1
        ciphersplit.append(ctext)
    
    j = 1
    for i in ciphersplit:
        for k in range(len(rank)):
            if j == rank[k]:
                for l in range(len(i)):
                    mat[l][k] = i[l]
        j += 1
    decipher = ""
    for i in mat:
        for j in i:
            decipher += j
    return decipher
    
# # Single
# text = "HELLOMEOWMEOW".upper()
# key = "ZEBRAS".upper()
# print(f"Plain Text : {text}")
# print(f"Key text : {key}")

# rank = ranker(key)
# mat = matBuilder(text, key)
# cipher = matTrasposer(mat, rank)
# print(f"Cipher Text : {cipher}")

# decipher = reverseTrasposer(cipher, rank)
# print(f"Decipher Text : {decipher}")

# Double
text = "HELLOMEOWMEOW".upper()
key1 = "ZEBRAS".upper()
key2 = "HEALTH".upper()
rank1 = ranker(key1)
rank2 = ranker(key2)
print(f"Plain Text : {text}")
print(f"Key 1 text : {key1}")
print(f"Key 2 text : {key2}")
mat1 = matBuilder(text, key1)
cipher1 = matTrasposer(mat1, rank1)
print(f"Cipher 1 : {cipher1}")
mat2 = matBuilder(cipher1, key2)
cipher2 = matTrasposer(mat2, rank2)
print(f"Cipher 2 : {cipher2}")
decipher1 = reverseTrasposer(cipher2, rank2)
print(f"Decipher 1 : {decipher1}")
decipher2 = reverseTrasposer(decipher1, rank1)
print(f"Decipher 2 : {decipher2}")