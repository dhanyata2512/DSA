class Node:
    def __init__(self,key):
        self.key=key
        self.l_child=None
        self.r_child=None

question=int(input("which treversal would you like to do on your tree: \n 1- create BST \n 2- Insert Node \n 3- Inorder Treversal \n 4- Preorder Treversal \n 5- Postorder Treversal \n 6- Exit \n "))

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


que1=int(input("How many nodes would you like to create: ")) 

root=None

for i in range(que1):
    n=int(input("Enter the key of the Node: "))
    root=insert(root,n)
#inorder_treversal(root)

while question == 6:
    if question == 1:
        insert(root,n)

    elif question == 2:
        insert(root,n)

    elif question == 3:
        inorder_treversal(root)
    elif question == 4:
        preorder_treversal
    elif question == 5:
        postorder_treversal
    elif question==6:
        quit()       
else:
    print("The number you have entered is not an known treversal...\n Please try again later\n :(")   


