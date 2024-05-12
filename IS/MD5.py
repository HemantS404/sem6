def f(b, c, d):
    return hex((int(b, 16) & int(c, 16)) | (~int(b, 16) & int(d, 16)))

text = "Hello my name is Hemant!!!"
print(f"Plain Text : {text}")

t = [bin(ord(i))[2:] for i in text]

text_bin = ""
for i in t:
    text_bin += i
len_text = len(text_bin)

required_padding = (512 - 64) - len_text%512
padded_text = text_bin + "1" + "0"*(required_padding - 1)
padded_text = padded_text + "0"*(64 - len(bin(len_text)[2:])) + bin(len_text)[2:]

A, B, C, D = "0x01234567", "0x89ABCDEF", "0xFEDCBA98", "0x76543210"

a, b, c, d = A, B, C, D

message_seg = [padded_text[i : 32+i] for i in range(0, 512, 32)]

keys = ['0xe0a5e0a5', '0x465a465a', '0xf737d44a', '0x6728bd47', 
        '0xb779d44a', '0x470bd44a', '0x34f2d44a', '0xbd47bd47', 
        '0xc7ab1a7f', '0xd44ad44a', '0xaa85bd47', '0x1f91d44a', 
        '0x6e541a7f', '0xdb1f1a7f', '0x13961a7f', '0x1a7f1a7f']

for i in range(16):
    f_bcd = f(b, c, d)
    a = hex((int(a, 16) + int(f_bcd, 16))%(int("0xffffffff", 16)))
    a = hex((int(a, 16) + int(message_seg[i], 2))%(int("0xffffffff", 16)))
    a = hex((int(a, 16) + int(keys[i], 16))%(int("0xffffffff", 16)))
    a_bin = bin(int(a, 16))[2:]
    a = a_bin[5:] + a_bin[:5] # s = 5
    a = hex((int(a, 16) + int(b, 16))%int("0xffffffff", 16))
    a, b, c, d = d, a, b, c

hash_message = ""
for i in [a, b, c, d]:
    j = i[2:]
    hash_message += "0"*(4 - len(j)) + i[2:]

print(f"Hased Message(MD5) : {hash_message}")