class nodes: 

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insertItems(root, n):
    if root == None:
        return nodes(n)
    if root.val > n: 
        root.left = insertItems(root.left, n)
    else: 
        root.right = insertItems(root.right, n)
    return root 

def search(root, x):
    if root.val == x: 
        return root
    elif root.val>x and root.left is not None: 
        return search(root.left, x) 
    elif root.val<x and root.right is not None: 
        return search(root.right, x)
    else:
        return -1

mibi = int(input("How many items?"))
root= None
for i in range(mibi):
    pr = int(input("What value do u want?"))
    root= insertItems(root, pr)




-------------------------------------------------------------------------------------
class nodes: 

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insertItems(root, n):
    if root == None:
        return nodes(n)
    if root.val > n: 
        root.left = insertItems(root.left, n)
    else: 
        root.right = insertItems(root.right, n)
    return root 

def search(root, x):
    if root.val == x: 
        return root
    elif root.val>x and root.left is not None: 
        return search(root.left, x) 
    elif root.val<x and root.right is not None: 
        return search(root.right, x)
    else:
        return -1

mibi = int(input("How many items?"))
root= None

def inOrder(root):
    if (root is not None):
        if root.left is not None:
            inOrder(root.left)
        print (root.val)
        if root.right is not None: 
            inOrder(root.right) 


for i in range(mibi):
    pr = int(input("What value do u want?"))
    root= insertItems(root, pr)
#inorder traversal

inOrder(root)
searchVal = int(input("Wht value to search?"))
vaal = search(root, searchVal)
if vaal == -1: 
    print("Not found")
else:
    print("Found ")
    print(vaal.val)

    
