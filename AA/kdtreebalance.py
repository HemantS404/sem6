data_array = [(7,8), (12,3), (14,1), (4,12), (9,1), (2,7), (10,19)]
n = len(data_array[0])

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class KDTree:

    def __init__(self, n):
        self.n = n
        self.root = None

    def buildSubroutine(self, par, d, k, direction):
        if len(d) == 0:
            return
        
        d = sorted(d, key = lambda i:i[k])
        mid = len(d)//2
        d_left = d[ : mid]
        d_right = d[mid+1 : ]

        if direction == 'L':
            par.left = Node(d[mid])
            par = par.left
        else:
            par.right = Node(d[mid])
            par = par.right

        self.buildSubroutine(par, d_left, (k+1)%self.n, 'L')
        self.buildSubroutine(par, d_right, (k+1)%self.n, 'R')

    
    def build(self, d):
        d = sorted(d, key = lambda i:i[0])
        mid = len(d)//2
        d_left = d[ : mid]
        d_right = d[mid+1 : ]
        self.root = Node(d[mid])
        self.buildSubroutine(self.root, d_left, (1)%self.n, 'L')
        self.buildSubroutine(self.root, d_right, (1)%self.n, 'R')

    def printTree(self, node, depth):
        if node == None:
            return
        else:
            print(node.data)
            if node.left != None:
                print("\t"*(depth+1), "L == ", end='')
                self.printTree(node.left, depth+1)
            if node.right != None:
                print("\t"*(depth+1), "R == ", end='')
                self.printTree(node.right, depth+1)


kdtree = KDTree(2)
kdtree.build(data_array)
kdtree.printTree(kdtree.root, 0)