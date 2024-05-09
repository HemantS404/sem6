class Node:
    def __init__(self, data, color):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.par = None
        self.is_DB = False


def printTree(node, depth):
    if node == None:
        return
    else:
        print(f"({node.data}, {node.color}, {node.is_DB})")
        if (node.left != None):
            print("\t"*(depth+1), "L == ", end="")
            printTree(node.left, depth+1)
        if (node.right != None):
            print("\t"*(depth+1), "R == ", end="")
            printTree(node.right, depth+1)

# case 1 (Red node) 
root = Node(55, "B")

root.left = Node(27, "B")
root.left.par = root

root.right= Node(66, "B")
root.right.par = root

root.left.left = Node(19, "R")
root.left.left.par = root.left

root.left.right= Node(51, "R")
root.left.right.par = root.left

root.right.right = Node(83, "R")
root.right.right.par = root.right

def predFinder(node):
    node = node.right
    while(node.left != None):
        node = node.left
    return node

def deleteNode(node, val):
    if node == None:
        return None
    
    elif (node.data != val):
        if node.data > val:
            return deleteNode(node.left, val)
        else:
            return deleteNode(node.right, val)
    else:
        if node.left == None and node.right == None:
            if node.color == "R":
                par = node.par
                if par.left == node:
                    par.left = None
                else:
                    par.right = None
                del node
                return None
            else:
                node.is_DB = True
                node.data = None
                return node

        elif node.left != None and node.right == None:
            node.data = node.left.data
            return deleteNode(node.left, node.left.data)
        elif node.left == None and node.right != None:
            node.data = node.right.data
            return deleteNode(node.right, node.right.data)
        else:
            pred = predFinder(node)
            node.data = pred.data
            return deleteNode(node.right, pred.data)

# # delete (51 , 27)
# printTree(root, 0)
# print("--------------------------")
# deleteNode(root, 51)
# printTree(root, 0)
# print("--------------------------")
# deleteNode(root, 27)
# printTree(root, 0)

# case 2 (root DB)
root.is_DB = False 

# case 3 (DB's sibling black and both sibling's child black or None child)
root = Node(10, "B")

root.left = Node(5, "B")
root.left.par = root

root.right= Node(20, "R")
root.right.par = root

root.right.left = Node(15, "B")
root.right.left.par = root.right

root.right.right = Node(30, "B")
root.right.right.par = root.right

def case3(node):
    par = node.par
    sibling = par.left if par.left != node else par.right

    def check(node):
        if node.left == None and node.right == None:
            return True
        elif (node.left != None and node.color == "B") or  (node.right != None and node.color == "B"):
            return True
        return False

    if sibling.color == 'B' and check(sibling):
        
        sibling.color = 'R'
        if par.color == 'B':
            par.is_DB = True
        else:
            par.color = 'B'
        
        if par.left == node:
            par.left = None
            del node
        else:
            par.right = None
            del node

        if par.is_DB:
            return par
        else:
            None
    
# printTree(root, 0)
# print("--------------------------")
# node = deleteNode(root, 20)
# case3(node)
# printTree(root, 0)

# case 4 (DB's sibling Red)
root = Node(10, "B")

root.left = Node(5, "B")
root.left.par = root

root.left.left = Node(1, "B")
root.left.left.par = root.left

root.left.right= Node(7, "B")
root.left.right.par = root.left

root.right= Node(20, "B")
root.right.par = root

root.right.left = Node(15, "B")
root.right.left.par = root.right

root.right.right = Node(30, "R")
root.right.right.par = root.right

root.right.right.left = Node(25, "B")
root.right.right.left.par = root.right.right

root.right.right.right = Node(40, "B")
root.right.right.right.par = root.right.right

def case4(node):
    par = node.par
    (sibling, is_left) = (par.left, True) if par.left != node else (par.right, False)
    if sibling.color == 'R':
        par.color = 'R'
        sibling.color = 'B'
        sibling.par = par.par
        if par.par.left == par:
            par.par.left = sibling
        else:
            par.par.right = sibling

        par.par = sibling
        
        if not is_left:
            extra = sibling.left
            sibling.left = par
            par.right = extra
        else:
            extra = sibling.right
            sibling.right = par
            par.left = extra
        
        if extra!=None:
            extra.par = par

# printTree(root, 0)
# print("--------------------------")
# node = deleteNode(root, 15)
# case4(node)
# printTree(root, 0)
# print("--------------------------")
# case3(node)
# printTree(root, 0)
# print("--------------------------")

# case6 (DB Sibling's far child red)
root = Node(65, "B")

root.left = Node(15, "B")
root.left.par = root

root.right = Node(68, "B")
root.right.par = root

root.right.right = Node(70, "R")
root.right.right.par = root.right

def case6(node):
    global root
    par = node.par
    (sibling, is_left) = (par.left, True) if par.left != node else (par.right, False)
    if not is_left and sibling.right.color == 'R':
        par.color, sibling.color = sibling.color, par.color
        if par == root:
            root = sibling

            temp = sibling.left

            sibling.left = par
            par.par = sibling
            sibling.right.color = "B"
            if par.left.data == None:
                par.left = None
            else:
                par.left.is_DB = False
            par.right = temp
            del node

# printTree(root, 0)
# print("--------------------------")
# node = deleteNode(root, 15)
# case6(node)
# printTree(root, 0)
# print("--------------------------")

#case5(DB Sibling's near child red)
root = Node(10, "B")

root.left = Node(5, "B")
root.left.par = root

root.left.left = Node(1, "B")
root.left.left.par = root.left

root.left.right= Node(7, "B")
root.left.right.par = root.left

root.right= Node(30, "B")
root.right.par = root

root.right.left = Node(25, "R")
root.right.left.par = root.right

root.right.left.left = Node(20, "B")
root.right.left.left.par = root.right.left

root.right.left.right = Node(28, "B")
root.right.left.right.par = root.right.left

root.right.right = Node(40, "B")
root.right.right.par = root.right

def case5(node):
    par = node.par
    (sibling, is_left) = (par.left, True) if par.left != node else (par.right, False)
    if not is_left and sibling.left.color == 'R':
        child = sibling.left
        sibling.color, child.color = child.color, sibling.color
        
        par.right = child
        child.par = par

        temp = child.right

        child.right = sibling
        sibling.par = child

        sibling.left = temp
        temp.par = sibling

# printTree(root, 0)
# print("--------------------------")
# node = deleteNode(root, 1)
# node = case3(node)
# case5(node)
# printTree(root, 0)
# print("--------------------------")
# case6(node)
# printTree(root, 0)
# print("--------------------------")
