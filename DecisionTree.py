class nodes:

    def __init__(self, val,):
        self.val = val
        self.left = None
        self.right = None

root = nodes("A")
root.left = nodes("B")
root.right = nodes("C")

root.left.left = nodes("D")
root.left.right = nodes("E")

#Inorder traversal- Left -- Middle -- Right 
def inOrder(node):
    if node:
        inOrder(node.left)
        print(node.val, end = " ")
        inOrder(node.right)

print("inOrder traversal " )
inOrder(root)


#Preorder - Middle -- Left -- Right
def preOrder(node):
    if node: 
        print(node.val, end= " ")
        inOrder(node.left)
        inOrder(node.right)

print("Preorder Traversal")
preOrder(root)

#Postorder - Left -- Right -- Middle
def postOrder(node):
    if node:
        postOrder(node.left)
        postOrder(node.right)
        print(node.val, end= " ")

print("PostOrder Traversal ")
postOrder(root)
