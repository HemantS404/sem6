text = "HELLO".upper()
key = "MEOWY".upper()

cipher = ""
for i in range(len(text)):
    ctext = (ord(text[i]) - ord("A"))^(ord(key[i]) - ord("A"))