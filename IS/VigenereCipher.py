text = "HELLOHEMANT".upper()
key = "WHY".upper()

print(f"Plain Text : {text}")
print(f"Key Text : {key}")

expanded_key = key*(len(text)//len(key)) + key [:len(text) % len(key)]
ciphersplit = []
for i in range(len(text)):
    ctext = chr(((ord(text[i]) - ord("A")) + (ord(expanded_key[i]) - ord("A")))%26 + ord("A"))
    ciphersplit.append(ctext)

cipher = ""
for i in ciphersplit:
    cipher += i
print(f"Cipher Text : {cipher}")

decipher = ""
for i in range(len(cipher)):
    dtext = chr(((ord(cipher[i]) - ord("A")) - (ord(expanded_key[i]) - ord("A")))%26 + ord("A"))
    decipher += dtext
print(f"Decipher Text : {decipher}")