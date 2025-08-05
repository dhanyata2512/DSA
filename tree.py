class Node():
    def __init__(self,key):
        self.key=key
        self.l_child=None
        self.r_child=None

question=int(input("which treversal would you like to do on your tree: \n 1- inorder treversal \n 2- preorder treversal \n 3- postorder trversal \n"))

def inorder_treversal(root):
    if root.l_child is not None: # There is a left child present
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


root=Node(2)
root.l_child=Node(3)
root.r_child=Node(13)
root.l_child.l_child=Node(4)
root.l_child.r_child=Node(7)
root.r_child.l_child=Node(6)
root.r_child.r_child=Node(14)


if question == 1:
    inorder_treversal(root)

elif question == 2:
    preorder_treversal(root)
   
elif question == 3:
    postorder_treversal(root)  
else:
    print("The number you have entered is not an known treversal...\n Please try again later\n :(")   

