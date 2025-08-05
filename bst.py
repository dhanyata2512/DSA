class Node:
    def __init__(self,key):
        self.key=key
        self.l_child=None
        self.r_child=None

def inorder_treversal(root):
    if root.l_child is not None:
        inorder_treversal(root.l_child)
    print(root.key)
    if root.r_child is not None:
        inorder_treversal(root.r_child) 

def insert(root,value):
    if root is None:
        return Node(value)
    if value < root.key:
        root.l_child=insert(root.l_child,value)
    else:
        root.r_child=insert(root.r_child,value)
    return root     


que1=int(input("How many nodes would you like to create: ")) 

root=None

for i in range(que1):
    n=int(input("Enter the key of the Node: "))
    root=insert(root,n)
inorder_treversal(root)       
