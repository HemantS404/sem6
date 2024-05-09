import math

size = 1
ele = 0
total_amortized_cost = 0
n = 9
#potential-func = 2i - cap)
def potential(i, cap):
    return (2*i - cap)

print("Element\tElements-in-Table\tSize\tCost\tAmortized-cost\tTotal-cost")
for i in range(n):
    old_size = size 
    cost = 1
    ele += 1
    if ele > size:
        cost += size
        size *= 2
    amortized_cost = cost + (potential(old_size + 1, size) - potential(old_size, old_size))

    total_amortized_cost += amortized_cost

    print(f"{i}\t{ele}\t\t\t{size}\t{cost}\t{amortized_cost}\t\t{total_amortized_cost}")

print("Total Cost :",total_amortized_cost) 
