text = "HELLOHEMANTXYZ".upper()
print(f"Plain Text : {text}")

a = [ord(i) - ord('A') for i in text]
b = [(i + 3)%26 for i in a]

cipher = ""
for i in b:
    cipher += chr(i + ord("A"))
print(f"Cipher Text : {cipher}")

c = [ord(i) - ord("A") for i in cipher]
d = [(i - 3)%26 for i in c]

decipher = ""
for i in d:
    decipher += chr(i + ord("A"))
print(f"Decipher Text : {decipher}")