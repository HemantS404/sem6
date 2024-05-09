class Node:
    def __init__(self, data):
        self.data = data
        self.color = "R"
        self.left = None
        self.right = None
        self.par = None


class RBTree:
    def __init__(self):
        self.root = None

    def RR(self, grandPar, par, child):
        pass
    def RL(self, grandPar, par, child):
        pass

    def LL(self, grandPar, par, child):
        grandParRight = grandPar.right
        
        grandPar.data, par.data = par.data, grandPar.data

        grandPar.right = par
        grandPar.left = child
        child.par = grandPar
        par.left = None

        par.right = grandParRight
        if (grandParRight != None):
            grandParRight.par = par

    def LR(self, grandPar, par, child):
        par.data, child.data = child.data, par.data
        par.left = child
        par.right = None
        self.LL(grandPar, par, child)
    
    def insertSubroutine(self, par, child):
        if par.data > child.data:
            if(par.left == None):
                par.left = child
                child.par = par
            else:
                self.insertSubroutine(par.left, child)
        else:
            if(par.right == None):
                par.right = child
                child.par = par
            else:
                self.insertSubroutine(par.right, child)

    def insert(self, data):
        node = Node(data)

        # case 1.a (Root is None)
        if self.root == None:
            self.root = node
            self.root.color = "B"
        
        # case 1.b (Parent Black)
        else:
            self.insertSubroutine(self.root, node)

        # (Parent red, child red)
        while(node.color == 'R' and node.par.color == "R"):
            par = node.par
            grandPar = par.par
            uncle = grandPar.left if grandPar.left != par else grandPar.right

            # case 2 (Uncle red)
            if (uncle != None) and (uncle.color == "R"):
                uncle.color = "B"
                par.color = "B"
                grandPar.color = "R"
            
            # case 3 (Uncle Black or None)
            else:
                if grandPar.left == par and par.left == node:
                    self.LL(grandPar, par, node)
                elif grandPar.left == par and par.right == node:
                    self.LR(grandPar, par, node)
                elif grandPar.right == par and par.right == node:
                    self.RR(grandPar, par, node)
                elif grandPar.right == par and par.left == node:
                    self.RL(grandPar, par, node)
                else:
                    print("Error")
                    break

        if (self.root.color == "R"):
            self.root.color = "B"


    def printTree(self, node, depth):
        if node == None:
            return
        else:
            print(f"({node.data}, {node.color})")
            if (node.left != None):
                print("\t"*(depth+1), "L == ", end="")
                self.printTree(node.left, depth+1)
            if (node.right != None):
                print("\t"*(depth+1), "R == ", end="")
                self.printTree(node.right, depth+1)

rbtree = RBTree()
rbtree.insert(55)
rbtree.insert(66)
rbtree.insert(27)
rbtree.insert(19)
rbtree.insert(51)
rbtree.insert(83)
rbtree.insert(57)
rbtree.insert(728)
rbtree.insert(7)
rbtree.insert(12)
rbtree.printTree(rbtree.root, 0)