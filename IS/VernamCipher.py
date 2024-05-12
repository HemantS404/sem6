text = "RAMSWARUPK".upper()
key = "RANCHOBABA".upper()
print(f"Plain Text : {text}")
print(f"Key Text : {key}")

cipher = ""
for i in range(len(text)):
    ctext = chr(((ord(text[i]) - ord("A"))^(ord(key[i]) - ord("A")))%26 + ord("A"))
    cipher += ctext
print(f"Cipher Text : {cipher}")

decipher = ""
for i in range(len(cipher)):
    dtext = chr(((ord(cipher[i]) - ord("A"))^(ord(key[i]) - ord("A")))%26 + ord("A"))
    decipher += dtext
print(f"Decipher Text : {decipher}")
