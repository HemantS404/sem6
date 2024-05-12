text = int(input("Enter number to be ciphered : "))
p = int(input("Enter P : "))
q = int(input("Enter Q : "))

print(f"\nP : {p} & Q : {q}")

phi_n = (p - 1)*(q - 1)
n = p*q
print(f"PHI(N) : {phi_n} & N : {n}")

def isPrime(ele):
    for i in range(2, int(ele**(1/2)) + 1):
        if ele%i == 0:
            return False
    return True

for e in range(n - 1, 2, -1):
    if e != p and e != q and isPrime(e):
        break

for d in range(2, n):
    if e!=d and (d*e) % phi_n == 1:
        break

print(f"Public Key (E) : {(e, n)}")
print(f"Private Key (D) : {(d, n)}")

cipher = (text**e)%n
print(f"\nCipher number : {cipher}")

decipher = (cipher**d)%n
print(f"Decipher number : {decipher}")