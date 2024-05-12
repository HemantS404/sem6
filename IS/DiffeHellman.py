g = int(input(f"Enter G : "))
p = int(input(f"Enter P : "))
a = int(input(f"\nEnter A : "))
b = int(input(f"Enter B : "))

print(f"\nG : {g} & P : {p}")
print(f"A : {a} & B : {b}")

X_a = (g**a) % p 
X_b = (g**b) % p
print(f"\nX(a) : {X_a} & X(b) : {X_b}")
print(f"\nA send [X(a) : {X_a}] to B")
print(f"B send [X(b) : {X_b}] to A")

A_x = (X_a**b) % p
B_x = (X_b**a) % p
print(f"\nA(x) : {A_x} & B(x) : {B_x}")
print(f"\nA calculate A(x) : {A_x}")
print(f"B calculate B(x) : {B_x}")

if A_x == B_x:
    print(f"\nKey Exchange Succesfull\nSecert Key : {A_x}")
else:
    print("Error")