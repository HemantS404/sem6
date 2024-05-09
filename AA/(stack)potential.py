class Potential:
    def __init__(self):
        self.stack = []
        self.size = 0
        self.total_amortized_cost = 0

    def push(self, x):
        cost = 1
        self.stack.append(x)
        amortized_cost = cost + ((self.size+1) - (self.size))
        self.size += 1
        self.total_amortized_cost += amortized_cost
        print(f"Push\t\t{cost}\t\t{amortized_cost}\t\t{self.total_amortized_cost}")

    def pop(self):
        if len(self.stack)!=0:
            cost = 1
            self.stack.pop()
            amortized_cost = cost + ((self.size - 1) - (self.size))
            self.size -= 1
            self.total_amortized_cost += amortized_cost
            print(f"Pop\t\t{cost}\t\t{amortized_cost}\t\t{self.total_amortized_cost}")

    def multipop(self, k):
        n = len(self.stack)
        if k <= n:
            cost = k
            for _ in range(k):
                self.stack.pop()
            amortized_cost = cost + ((self.size - k) - (self.size))
            self.size -= k
            self.total_amortized_cost += amortized_cost
        else:
            cost = n
            for _ in range(n):
                self.stack.pop()
            amortized_cost = cost + ((self.size - n) - (self.size))
            self.size -= n
            self.total_amortized_cost += amortized_cost
        print(f"MuiltiPop\t{cost}\t\t{amortized_cost}\t\t{self.total_amortized_cost}")

a = Potential()

print("Operations\tActual-Cost\tAmortized-Cost\tTotal-Cost")
for i in range(9):
    a.push(i)

for _ in range(3):
    a.pop()

for _ in range(3):
    a.multipop(2)

print(f"Total Amortized Cost : {a.total_amortized_cost}")