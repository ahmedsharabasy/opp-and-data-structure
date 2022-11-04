class node:                   # A class that represents an individual node in a Binary Tree 
    def __init__(self,key):   #key=value of node
        self.left=None
        self.right=None
        self.val=key

def print_in_order(root):       
    if root:
        print_in_order(root.left)
        print(root.val)
        print_in_order(root.right)    

def print_pre_order(root):
    if root:
        print(root.val)
        print_pre_order(root.left)
        print_pre_order(root.right)


def print_post_order(root):
    if root:
        print_post_order(root.left)
        print_post_order(root.right)
        print(root.val)

root = node(1) 
root.left = node(2) 
root.right = node(3) 
root.left.left = node(4) 
root.left.right = node(5) 
print ("Preorder traversal of binary tree is")
print_pre_order(root) 
  
print ("\nInorder traversal of binary tree is")
print_in_order(root) 
  
print ("\nPostorder traversal of binary tree is")
print_post_order(root)         

