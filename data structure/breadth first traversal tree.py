class Node:                  
    def __init__(self,key):   
        self.left=None
        self.right=None
        self.val=key


def print_given_level(root,level):             #يطبع الليفل الواحد بس 
    if root is None:
        return
    if level == 1:
        print(root.val,end="  ")
    elif level > 1 :
        print_given_level(root.left , level-1)
        print_given_level(root.right , level-1)


def height(node):                #Node=root         #الفانكشن بتعرفنى عندى كام ليفل
    if node is None :
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight :
            return lheight+1    #+1عشان بيبدا عد من الصفر
        else:
            return rheight+1        


def print_level_order(root):                       #يطبع كل الليفيلات
    h=height(root)
    for i in range(1,h+1):
        print_given_level(root,i)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print("Level order traversal of binary tree is :")
print_level_order(root)
