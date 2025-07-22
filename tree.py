class Node():
    def __init__(self,key):
        self.key=key
        self.l_child=None
        self.r_child=None

root=Node(2)
root.l_child=Node(3)
root.r_child=Node(13)
root.l_child.l_child=Node(4)
root.l_child.r_child=Node(7)
root.r_child.l_child=Node(6)
root.r_child.r_child=Node(14)        
