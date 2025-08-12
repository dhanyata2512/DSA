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

def preorder_treversal(root):
    print(root.key)
    if root.l_child is not None:
        preorder_treversal(root.l_child)
    if root.r_child is not None:
        preorder_treversal(root.r_child)

def postorder_treversal(root):
    if root.l_child is not None:
        postorder_treversal(root.l_child)
    if root.r_child is not None:
        postorder_treversal(root.r_child)
    print(root.key)


def insert(root,value):
    if root is None:
        return Node(value)
    if value < root.key:
        root.l_child=insert(root.l_child,value)
    else:
        root.r_child=insert(root.r_child,value)
    return root 

def search(root,value):
    if root.key == value:
        return True
    elif value < root.key and root.l_child is not None:
        return search(root.l_child,value)
    elif value > root.key and root.r_child is not None:
        return search(root.r_child, value)
    else:
        return False
def inorder_succ(node):
    succ=node.r_child
    while succ.l_child is not None:
        succ=succ.l_child
    return succ
        

def delete(root,value):
    if root is None:
        return root
    if root.key > value:
        root.l_child =delete(root.l_child,value)
    elif root.key < value:
        root.r_child = delete(root.r_child,value)
    else:
        if root.l_child is None:
            return root.r_child
        
        if root.r_child is None:
            return root.l_child 
        gotten=inorder_succ(root) 
        root.key=gotten.key
        root.r_child =delete(root.r_child,gotten.key)
    return root
               
    
que1=int(input("How many nodes would you like to create: "))

root=None

for i in range(que1):
    n=int(input("Enter the key of the Node: "))
    root=insert(root,n)
inorder_treversal(root)
find=int(input("What value would you like to search for: "))
print(search(root,find))
delete_num=int(input("What value would you like to delete: "))
delete(root,delete_num)
inorder_treversal(root)



