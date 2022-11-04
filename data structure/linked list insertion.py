class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:        
    def __init__(self):
        self.head=None         #head is in the first

    def push(self,item):       # Function to insert a new node at the beginning 
        newnode=Node(item)
        newnode.next=self.head
        self.head=newnode

    def insertafter(self,per_node,item):          #insert middle
        if per_node==None:
            return print("The given previous node must be in LinkedList")    
        newnode=Node(item)
        newnode.next=per_node.next 
        per_node.next=newnode      #llist.insertafter(llist.head.next,99)

    def append(self,item):     # Appends a new node at the end.
        newnode=Node(item)
        if self.head==None:
            self.head=newnode
            return     
        rear=self.head
        while rear.next:       #because the is in the first
            rear=rear.next
        rear.next=newnode        

    def printlist(self):
        temp=self.head
        print('created linked list is:\n',end='')
        while temp:
            print(temp.data)
            temp=temp.next


        
if __name__=="__main__":
    llist=linkedList()
    llist.append(1)
    llist.append(2)
    llist.push(44)
    llist.append(6)
    llist.push(55)
    llist.push(3)
    llist.push(4)
    llist.append(5)
    llist.printlist()
    print('*'*50)
    llist.insertafter(llist.head.next.next,99)
    llist.printlist()