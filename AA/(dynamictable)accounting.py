size = 1
ele = 0
n = 17
balance = 0
insert_charge = 3

print("Element\tElements-in-Table\tSize\tCost\tInsertion-Charge\tBalance")
for i in range(n):
    cost = 1
    ele += 1
    if ele > size:
        cost += size
        size *= 2
    balance -= cost - insert_charge
    print(f"{i}\t{ele}\t\t\t{size}\t{cost}\t{insert_charge}\t\t\t{balance}")

print("Total Balance :",balance)
        