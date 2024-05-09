class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class KDTree:
    def __init__(self, n):
        self.root = None
        self.n = n

    def insertSubroutine(self, par, child, k):
        if par.data[k] > child.data[k]:
            if par.left == None:
                par.left = child
            else:
                self.insertSubroutine(par.left, child, (k+1)%self.n)
        else:
            if par.right == None:
                par.right = child
            else:
                self.insertSubroutine(par.right, child, (k+1)%self.n)

    
    def insert(self, data):
        new_node = Node(data)

        if self.root == None:
            self.root = new_node
        else:
            self.insertSubroutine(self.root, new_node, 0)

    def printTree(self, node, depth):
        if node == None:
            return
        else:
            print(node.data)
            if node.left != None:
                print("\t"*(depth+1), "L == ", end='')
                self.printTree(node.left, depth+1)
            if node.right != None:
                print(" \t"*(depth+1), "R == ", end='')
                self.printTree(node.right, depth+1)

data_array = [(30,40), (5,25), (10,12), (70,70), (50,30), (35,45)]
# data_array = [(7,8,1), (12,3,2), (14,1,3), (4,12,4), (9,1,5), (2,7,6), (10,19,7)]
n = len(data_array[0])

kdtree = KDTree(n)
for data in data_array:
    kdtree.insert(data)
kdtree.printTree(kdtree.root, 0)