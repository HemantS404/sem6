from math import atan2
import matplotlib.pyplot as plt

points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
n = len(points)

points = sorted(points, key = lambda i: i[0])
points = sorted(points, key = lambda i: i[1])
p = points[0]
points = sorted(points, key = lambda i: atan2(i[1] - p[1], i[0] - p[0]))
plt.scatter([i[0] for i in points], [i[1] for i in points])
plt.show()

stack = []
stack.append(points[0])
stack.append(points[1])
stack.append(points[2])

def angle(a, b, c):
    m1 = (b[1] - a[1])*(c[0] - a[0])
    m2 = (c[1] - a[1])*(b[0] - a[0])
    return m1-m2

for i in range(3, n):
    while angle(stack[-2], stack[-1], points[i]) > 0:
        stack.pop()
    stack.append(points[i])

print(stack)

for i in range(len(stack) - 1):
    plt.plot([stack[i][0], stack[i+1][0]], [stack[i][1], stack[i+1][1]])

plt.plot([stack[-1][0], stack[0][0]], [stack[-1][1], stack[0][1]])
plt.show()