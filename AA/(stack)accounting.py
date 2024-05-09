class Accounting:
    def __init__(self):
        self.stack = []
        self.push_charge = 2
        self.pop_charge = 0
        self.multipop_charge = 0
        self.balance = 0

    def push(self, x):
        push_cost = 1
        self.stack.append(x)
        self.balance -= push_cost - self.push_charge

    def pop(self):
        pop_cost = 1
        if len(self.stack) != 0:
            self.stack.pop()
            self.balance -= pop_cost - self.pop_charge

    def multipop(self, k):
        n = len(self.stack)
        if k <= n:
            multipop_cost = k
            for _ in range(k):
                self.stack.pop()
        else:
            multipop_cost = n
            for _ in range(n):
                self.stack.pop()

        self.balance -= multipop_cost - self.multipop_charge
a = Accounting()

print("Operation\tCharge\tCost\tBalance")
for i in range(9):
    a.push(i)
    print(f"Push\t\t2\t1\t{a.balance}")

for _ in range(3):
    a.pop()
    print(f"Pop\t\t0\t1\t{a.balance}")

for _ in range(3):
    k = 2
    a.multipop(k)
    print(f"Multipop\t0\t{k}\t{a.balance}")
        

print(f"Final balance : {a.balance}")