class Aggregate:
    def __init__(self):
        self.stack = []
        self.push_count = 0
        self.pop_count = 0
        self.multipop_count = 0
        self.totalcost = 0
    
    def push(self, x):
        self.stack.append(x)
        self.push_count += 1
        self.totalcost += 1

    def pop(self):
        if len(self.stack) != 0:
            self.stack.pop()
            self.pop_count += 1
        
        self.totalcost += 1 

    def multipop(self, k):
        n = len(self.stack)
        if k <= n:
            for _ in range(k):
                self.stack.pop()
            self.totalcost += k
        else:
            for _ in range(n):
                self.stack.pop()
            self.totalcost += n
        
        self.multipop_count += 1

a = Aggregate()
for i in range(9):
    a.push(i)

for _ in range(3):
    a.pop()

for _ in range(3):
    a.multipop(2)

print("Total Operations :", (a.push_count + a.pop_count + a.multipop_count))
print("Total cost :", a.totalcost)
print("Amortized Cost Per Operation :", (a.totalcost)/(a.push_count + a.pop_count + a.multipop_count))


