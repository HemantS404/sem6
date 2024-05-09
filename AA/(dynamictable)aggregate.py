size = 1
ele = 0
n = 17
total_cost = 0


print("Element\tElements-in-Table\tSize\tCost\tTotal Cost")
for i in range(n):
    cost = 1
    ele += 1
    if (ele > size):
        cost += size
        size *= 2
    total_cost += cost
    print(f"{i}\t{ele}\t\t\t{size}\t{cost}\t{total_cost}")

print(f"Total Operation : {n}")
print(f"Total Cost : {total_cost}")
print(f"Amortized Cost : {total_cost/n}")

        