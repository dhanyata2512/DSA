class Node():
    def __init__(self,key):
        self.key=key
        self.l_child=None
        self.r_child=None

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

inorder_treversal(root)
print("---------")
preorder_treversal(root)
print("---------")
postorder_treversal(root)

